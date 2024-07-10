#!/bin/bash

while true; do
    echo "File Management System"
    echo "----------------------"
    echo "1. Create a file"
    echo "2. append to an existing file"
    echo "3. Display file content"
    echo "4. Exit"
    read -p "choose an option: " option

    case $option in
        1)
            read -p "Enter the file name: " file_name
            read -p "Enter the content to write: " content
            echo "$content" > "$file_name"
            echo "File '$file_name' created with the following content: "
            cat "$file_name"
            echo
            ;;
        2)
            read -p "Enter file name to append content to: " file_name
            read -p "Enter the content you want to append: " content
            echo "$content" > "$file_name"
            echo "Appended the following content to '$file_name' :"
            echo "$content"
            echo
            ;;
        3)
            read -p "Enter the file name to display: " file_name
            if [ -f "$file_name" ]; then
                echo "content of '$file_name':"
                cat "$file_name"
            else
                echo "file '$file_name' does not exist"
            fi
            echo
            ;;
        4)
            echo "Exiting.."
            exit 0
            ;;
        *)
            echo "Invalid option. Please try again"
    esac
done