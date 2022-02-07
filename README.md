# MagicEden-Floor-Monitor

This is a pretty simple cli tool that monitors the floor price of the collection you selected so when you are paperhanding the 6th derivative collection of SMB this week you can make .2 SOL off it.

Requires you to put the collection name as magic eden's api would display the name so Defi Pirates would be defi_pirates. It'll print the current floor every 2 seconds. You can change the sleep time at the bottom of the infinite loop. If you wanna stop monitoring you can close the program, but since magic eden goes offline every 6 minutes give or take the json error you get will probably close it before.

Probably important to mention the rate limit of the api is 120 requests per minute so I set it to 2 seconds to allow you to be able to browse while using and still be able to list. 1 second would probably be better.

Feel free to tip me in solana hRKxv4G25TknkKwHvxd6TUkny4cB7tQ23XG9ZJ8LQw4 or fork this and actually make the code not abysmal.
