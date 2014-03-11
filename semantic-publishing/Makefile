# Makefile for Python client to Textalytics.com 1.0
#
# Copyright: Daedalus - Data, Decisions and Language  
# author: textalytics

CLIENT_VERSION = 1.0
API_VERSION = 1.0
API_NAME = sempub-$(API_VERSION)
NAME = textalytics-sdk-python-$(API_NAME)

# Target directory to perform the build 
TARGET_DIR = target

# Limpia el directorio local donde hace build
clean: 
	rm -rf $(TARGET_DIR)

package: clean
	mkdir -p $(TARGET_DIR)/$(NAME)/
	cp *.py $(TARGET_DIR)/$(NAME)/
	cp README.md $(TARGET_DIR)/$(NAME)/
	cp LICENSE $(TARGET_DIR)/$(NAME)/
	cd $(TARGET_DIR); tar -zcvf $(NAME).tar.gz $(NAME)/* 
