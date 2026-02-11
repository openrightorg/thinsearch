index-single.html: index.html thinsearch.js
	python3 inline_assets.py index.html > $@
