username = input('Hello, please create your username. ')
password = input(f'Hi, {username}. Please make a password. ')
pass_length = len(password)
secret_password = '*' * pass_length


print(f'Your password {secret_password} is {pass_length} characters long.')
