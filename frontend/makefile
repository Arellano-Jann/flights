run:
	npm run dev

add:
	pnpx shadcn-svelte@latest add 

open:
	npm run dev -- --open

node:
	# Remove node and NPM completely
	sudo rm -rf /usr/local/bin/npm 
	sudo rm -rf /usr/local/share/man/man1/node* 
	sudo rm -rf /usr/local/lib/dtrace/node.d
	rm -rf ~/.npm
	rm -rf ~/.node-gyp
	sudo rm -rf /opt/local/bin/node
	sudo rm -rf /opt/local/include/node
	sudo rm -rf /opt/local/lib/node_modules
	sudo rm -rf /usr/local/lib/node*
	sudo rm -rf /usr/local/include/node*
	sudo rm -rf /usr/local/bin/node*
	# sudo apt-get remove nodejs npm node
	# sudo apt-get purge nodejs

	# stops here

	# These should return nothing
	# which node 
	# which nodejs
	# which npm

	# Install nvm
	curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash
	export NVM_DIR="$HOME/.nvm"
	[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"  # This loads nvm
	[ -s "$NVM_DIR/bash_completion" ] && . "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

	# Stops here

	# Should return a number if success
	nvm --version

	# install both node and npm
	nvm install 18.15.0
	nvm use 18.15.0

	# check installation
	which npm
	which node

dep:
	make node
	npm install

build:
	npm run build
	npm run preview

all:
	make run