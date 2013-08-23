Blog
====

Project local installation instructions:
----------------------------------------

1. **Install virtualenvwrapper:**

    pip install virtualenvwrapper

2. **Create home venv variable:**

    export WORKON_HOME=~/Envs

3. **Create home venv dir:**

    mkdir $WORKON_HOME

4. **Activate venv wrapper (you may also add this command to .bashrc):**

    source /usr/local/bin/virtualenvwrapper.sh

5. **Make venv:**

    mkvirtualenv blog

    **Or switch to the venv, if you already created it earlier:**

    workon blog

6. **Clone the project:**

    git clone git@github.com:bo858585/blog.git

7. **Install packages:**

    pip install -r requirements.txt

8. **Set mysql password:**

    mysql -p -u root

    CREATE USER 'bloguser'@'localhost' IDENTIFIED BY 'blogpassword';

    GRANT all ON blog.* TO bloguser;

9. **Install bower:**

    sudo apt-get install npm

    sudo apt-get install nodejs

    sudo npm install bower -g

10. **Install bootstrap:**

    bower install bootstrap
