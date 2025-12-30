# Markdown Note-Taking App

This is a markdown note taking api. You can authenticate, upload your .md files, list all files, and access the html rendered version of your files.

## Requirements
This project requires:
- Django    5.2.8
- Python    3.13.11
- DRF       3.16.1
- Markdown  3.10

## Usage
- You upload the .md file (***less than 5 Mb***) to `/upload/`

- You list all your uploaded files by sending `GET` request to `/list/`

- You get the html form of your uploaded file by sending `GET` request to `/note/<file_id>` (***you get the file id in the reponse to the upload or in the list endpoint***)

## Contributing
All contributions are welcomed.

## License
This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.

## Project status
This project isn't being maintened.
