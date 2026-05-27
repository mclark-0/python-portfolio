import pandas as pd

df = pd.read_csv('hacker.csv')


df['Time'] = pd.to_datetime(df['Time'])
df = df.sort_values(by='Time')

print("--- Log Analysis Report ---\n")

failed_logins = df[df['status'] == 'failed']
successful_logins = df[df['status'] == 'success']

compromised_users = []
for user in failed_logins['Log_ID'].unique():
    user_failed = failed_logins[failed_logins['Log_ID'] == user]
    user_success = successful_logins[successful_logins['Log_ID'] == user]

    if not user_success.empty and not user_failed.empty:
        if user_success['Time'].min() > user_failed['Time'].max():
            compromised_users.append(user)

print(f"Compromised Account(s): {', '.join(compromised_users)}")


data_theft = df[df['Data_KB'] == 'data_transfer']

if not data_theft.empty:
    max_theft = data_theft.loc[data_theft['amount_stolen'].idxmax()]
    print(f"Data Stolen Time: {max_theft['Time']}")
    print(f"File Stolen: {max_theft['file_name']}")
    print(f"Amount Stolen: {max_theft['amount_stolen']} bytes")
else:
    print("No large data theft detected.")

password_resets = df[df['action'] == 'password_reset']['Log_ID'].nunique()
print(f"Users forced to reset passwords: {password_resets}")

