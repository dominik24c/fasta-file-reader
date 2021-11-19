### 1. Run Script
```bash
python3 main.py FASTA_FILE
```

### 2. Install packages
```bash
virtualenv venv
source venv/bin/activate
pip3  install -r requirements.txt
```

### 3. Add new packages to requirements.txt file
```bash
pip3 freeze > requirements.txt
```

### 4. Description of improvements
##### 1. Handling '-' dash sign - ignore it
##### 2. Handling '*' asterisk sign - stop translation
##### 3. Display bar graph of translated sequence
##### 4. Move data to data dir and add several fasta files from this [website][1]
[1]: https://www.ncbi.nlm.nih.gov/