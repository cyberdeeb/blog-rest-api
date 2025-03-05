from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import BlogPost

class BlogPostAPITest(APITestCase):

    def setUp(self):
        """Set up test data"""
        self.blogpost = BlogPost.objects.create(
            title = 'Test Post',
            content = 'This is a test post, this better work',
            tag = 'test'
        )

        self.blogpost_url = reverse('blogpost-list-create')

    def test_create_blogpost(self):
        """Test POST request to create a new blogpost"""

        data = {'title':'New Test Post', 'content': 'New test content', 'tag': 'new'}
        response = self.client.post(self.blogpost_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'New Test Post')
        self.assertEqual(response.data['content'], 'New test content')
        self.assertEqual(response.data['tag'], 'new')

    def test_get_blogposts(self):
        """Test GET request to retrieve all blogposts"""

        response = self.client.get(self.blogpost_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_get_blopost_id(self):
        """Test GET request to retrieve blogpost by ID"""

        retrieve_by_id_url = reverse('blogpost-update', args=[self.blogpost.id])
        response = self.client.get(retrieve_by_id_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Post')
        self.assertEqual(response.data['content'], 'This is a test post, this better work')
        self.assertEqual(response.data['tag'], 'test')

    def test_update_blogpost(self):
        """Test PUT request to update a blogpost"""

        update_url = reverse('blogpost-update', args=[self.blogpost.id])
        data = {"title": "Updated Title", "content": "Updated content", "tag": "updated"}
        response = self.client.put(update_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Title')
        self.assertEqual(response.data['content'], 'Updated content')
        self.assertEqual(response.data['tag'], 'updated')

    def test_delete_blogpost(self):
        """Test DELETE request to remove a blogpost"""
        delete_url = reverse('blogpost-update', args=[self.blogpost.id])
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(BlogPost.objects.filter(id=self.blogpost.id).exists())