import os

# install pip
# os.system("rm -rf /opt/homebrew/lib/python3.11/site-packages/*")
# os.system("curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py")
# os.system("python3 get-pip.py")

# install dependencies
python = "python3"
pip = "pip3.11 "

os.system(pip + "install jinja2")
os.system(pip + "install langid==1.1.6")
os.system(pip + "install numpy")
os.system(pip + "install pandas")
os.system(pip + "install regex")
os.system(pip + "install scikit-learn==0.24.1")
os.system(pip + "install sentence-transformers==1.0.4")
os.system(pip + "install tensorflow==2.6.0")
os.system(pip + "install tensorflow-hub>=0.12.0")
os.system(pip + "install tensorflow-text==2.6.0")
os.system(pip + "install keras==2.6")
os.system(pip + "install tokenizers==0.10.1")
os.system(pip + "install torch>=1.8.0")
os.system(pip + "install transformers>=4.15")
os.system(pip + "install tensorflow")
os.system(pip + "install gradio>=2.7")
os.system(pip + "uninstall -y gradio")
os.system(pip + "install gradio==2.7.5.2")
os.system(pip + "install typing-extensions --upgrade")

# exec app
os.system(python + " app.py")
