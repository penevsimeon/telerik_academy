import unittest

from models.comment import Comment


class Comment_Should(unittest.TestCase):
    def test_init_setProperties(self):
        # Arrange
        content = 'hello, mom!'
        author = 'steven'

        # Act
        comment = Comment(content, author)

        # Assert
        self.assertEqual(content, comment.content)
        self.assertEqual(author, comment.author)

    def test_init_raisesError_contentTooShort(self):
        # Arrange
        content = 'hi'
        author = 'steven'

        # Act
        with self.assertRaises(ValueError):
            Comment(content, author)

    def test_init_raisesError_contentTooLong(self):
        # Arrange
        content = 'x' * 201
        author = 'steven'

        # Act
        with self.assertRaises(ValueError):
            Comment(content, author)

    def test_str_returnsCorrectlyFormatted(self):
        # Arrange
        content = 'hello, mom!'
        author = 'steven'
        expected = '\n'.join([
            '----------',
            'hello, mom!',
            'User: steven',
            '----------',
        ])
        comment = Comment(content, author)

        # Act
        stringified = str(comment)

        # Assert
        self.assertEqual(expected, stringified)
