# !/usr/bin/env bash



git_init(){

    echo "READ" >> README.md
    git init
    git add README.md

    git commit -m "first commit"
    
    sleep 1
    git remote add origin $1
    git push -u origin master
}




create(){

    cd

    read -p "type your username: " username
    read -p "typer your password:" password

    export username
    export password


    python /Users/enriavil1/Desktop/project/Python/automation/create.py $1

    cd /Users/enriavil1/Desktop/project/Python/$1

    sleep 2
    git_init https://github.com/${username}/${1}.git

}

    




