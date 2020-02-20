# !/usr/bin/env bash



git_init(){
    echo "${name}">> README.md

    git init

    sleep 3

    git add README.md
    git commit -m "first commit"

    sleep 2
    git remote add origin $1
    git push -u origin master
}




create(){

    cd

    name = $1

    read -p "type your username: " username
    read -p "typer your password:" password

    export username
    export password


    python /Users/enriavil1/Desktop/project/Python/automation/create.py $1

    cd /Users/enriavil1/Desktop/project/Python/$1

    sleep 3


    git_init https://github.com/enriavil1/${1}.git


}

    




