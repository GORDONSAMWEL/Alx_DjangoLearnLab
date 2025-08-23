Update your README.md with examples like:

POST /api/posts/ → create post

GET /api/posts/?search=hello → search posts

POST /api/comments/ → add comment


Follow a user

POST /accounts/follow/<user_id>/

Unfollow a user

POST /accounts/unfollow/<user_id>/

Get feed

GET /api/feed/ → returns posts from followed users