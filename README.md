# Blog-Home
## Description
Blog-Home is a blog site that allow users to see different blogs posted by writers and add comments,like comments and create accounts to post different blog posts.

## Author
[CharityMutonii](https://github.com/CharityMutonii)

####  User view
* User can view the blog posts on the site
* User sees random quotes on the site
* User can view the most recent posts
* User can subscribe to blog mailing list and receives an email alert when a new post is made.
* User can comment on blog posts

####  Writer view
* sign in /Sign up to the blog.
* create a blog from the application.
* delete comments that I find insulting or degrading on my blog posts
* update or delete blogs I have created.


## Behavior Driven Development

| Input                    | Behaviour                       | Output                                       |
| -------------------------| ------------------------------  | -------------------------------------------- |
| Subscribe to the app              | Input your email               | Redirect you to the index page               |
| Writer login                    | Fill the login form           | Redirect you to the Homepage                 |
| Create a blog post by filling blog form          | Write your blog and post it to blogs    | Your blog is displayed with other blogs in index page                     |
| User comment on the Blog post and enter a desirable name | Write your comment and post it | Your comment is displayed under the blog post   |
| Writer delete a blog post       | Deleting the blog post from the database    | The blog post will be deleted and not appear on the page                  |
| Writer update a blog post       | Updating the blog post in database    | The blog post will be updated                |
| Writer delete a comment of his/her blog posts       | Deleting the blog post in database    | The comment will no longer appear under the post                   |

## Technologies Used
* Python
* Flask Framework
* PostgreSQL (database)
* HTML5  
* CSS
* Bootstrap
* Font Awesome
* jQuery
* Google Font API


## Setup/Installation Requirements
* Ensure that Python is installed on your machine if not please visit the python website and download the latest version python 3.6
* Fork the repository and either download the project or clone it to your machine
* Create a virtual environment using the following command
```
python3.6 -m venv --without-pip virtual
```
* then install the latest version of pip that will help you to install other needed modules
```
curl https://bootstrap.pypa.io/get-pip.py | python
```
* activate your virtual environment using :
```
source virtual/bin/activate
```
* In start.sh file register your three environmental variables as follows :
```
export SECRET_KEY=<your-secret-key>
```

* run the application from your terminal using the following command
```
chmod a+x start.sh
./start.sh
```


## Contact details
You can provide feedback or raise any issues/ bugs through the following means:
* charitytoni0@gmail.com

## Live Site link
You can view the live application by following this().

## License
#### This project is license  by MIT for more information visit [LICENSE.md](LICENSE.md) .
