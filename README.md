Blog
====

Project local installation instructions:
----------------------------------------

#. **Install virtualenvwrapper:**

    pip install virtualenvwrapper

#. **Create home venv variable:**

    export WORKON_HOME=~/Envs

#. **Create home venv dir:**

    mkdir $WORKON_HOME

#. **Activate venv wrapper (you may also add this command to .bashrc):**

    source /usr/local/bin/virtualenvwrapper.sh

#. **Make venv:**

    mkvirtualenv blog

    **Or switch to the venv, if you already created it earlier:**

    workon blog

#. **Clone the project:**

    git clone git@github.com:bo858585/blog.git

#. **Install packages:**

    pip install -r requirements.txt

#. **Set mysql password:**

    mysql -p -u root

    CREATE USER 'bloguser'@'localhost' IDENTIFIED BY 'blogpassword';

    GRANT all ON blog.* TO bloguser;
