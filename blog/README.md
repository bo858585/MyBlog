blog
====

<ol>
    <li>
        <h5>Install virtualenvwrapper:</h5>
        <div>pip install virtualenvwrapper</div>
    </li>
    <li>
        <h5>Create home venv variable:</h5>
        <div>export WORKON_HOME=~/Envs</div>
    </li>
    <li>
        <h5>Create home venv dir:</h5>
        <div>mkdir $WORKON_HOME</div>
    </li>
    <li>
        <h5>Activate venv wrapper:</h5>
        <div>source /usr/local/bin/virtualenvwrapper.sh (also you may add this command to .bashrc)</div>
    </li>
    <li>
        <h5>Make venv:</h5>
        <div>mkvirtualenv blog</div>
        <h5>Or switch to the venv, if you already created it:</h5>
        <div>workon blog</div>
    </li>
    <li>
        <h5>Install packages:</h5>
        <div>$WORKON_HOME/blog/bin/pip install django==1.5</div>
    </li>
    <li>
        <h5>Clone the project:</h5>
        <div>git clone git@github.com:bo858585/blog.git</div>
    </li>
    <li>
        <h5>Install mysql python lib:</h5>
        <div>$WORKON_HOME/blog/bin/pip install mysql-python</div>
    </li>
    <li>
        <h5>Set mysql password</h5>
        <div>mysql -p -u root</div>
        <div>CREATE USER 'bloguser'@'localhost' IDENTIFIED BY 'blogpassword';</div>
        <div>GRANT all ON blog.* TO bloguser;</div>
</oi>
