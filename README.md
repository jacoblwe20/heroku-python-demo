# Deploy Python Apps to Heroku

This is a small app that will run on Heroku, this app is made to demonstrate how easy it is to deploy apps to heroku.

## Setup

Heroku heavily uses `git` so you will need that installed and then you will need dowload their [toolbelt](https://toolbelt.heroku.com/). You will also need a [Heroku Account](https://id.heroku.com/signup/devcenter) its free.

If you have never use Heroku before on your computer you will need to run `heroku login` to log into you account from you computer.

For python you will need to use [pip](http://www.pip-installer.org/en/latest/installing.html) as your depedency manager, and `virtualenv` to control your enviroment.

#####  virtualenv

```
pip install virtualenv
```

When in the directory of you app run 

```
virtualenv venv --distribute
```

This will create a subdirectory to hold all your python modules. To activate the enviroment use.

```
source venv/bin/activate
```
Now you will have a ton of files that you will not need to push up to Heroku that are in your directory. We can ignore them by adding them to the end of your `.gitignore` file. Eg.

```
# Virtual Enviroment
venv
```

##### Port Binding

Heroku wants to tell your app which port to bind to. This is super simple to setup. Heroku does this by setting a enviroment variable `PORT`.

In your app for example it could be something like.

```python
app.run( port = int( os.getenv('PORT', 5000) ) );
```

## Startup

On your computer you can use anything to startup your app, but Heroku uses `Foreman` to startup apps. You can easily tell Foreman what to do by creating a procfile in the root of your directory. eg.

```
web : gunicorn index:app
```

You can test to see if it is working by using the command `foreman start`. You will not need to install `Foreman` it came bundled with the Heroku toolbelt.

## Creating App

First initialize git.

```
git init
```

After all the this settup you are now about ready to deploy the application up to Heroku. First tho you need to create an app on their service.

```
heroku create:app {app_name}
```

This should create the app on Heroku's server, and also add a git remote `heroku` to this repo.

## Deploy

Like mentioned above Heroku uses `git` to deploy. So you need to settup you app, or make a new commit to push up to Heroku.

```
git add --all
git commit -am "Initial Commit"
git push heroku master
```

You should see a stream of deploy information in your console, and then a url to see where you app is living.



