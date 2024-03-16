def get_user_with_max_nodes(node_dict):
  """Helper function to extract users with max nodes"""
  max_nodes = max(node_dict.values())
  users = []
  for user, nodes in node_dict.items():
    if nodes == max_nodes:
      users.append(user)
  return users

# File Handling
with open("log_file.txt", "r") as log_file:
  lines = log_file.readlines()
lines = lines[1:]  # Skip header

# Data structures
running_jobs_per_user = {}
pending_jobs_per_user = {}
max_nodes_per_user_running = {}
max_nodes_per_user_pending = {}
max_nodes_overall = 0

# Process each line
for line in lines:
  # ... (Rest of the parsing logic remains the same)

# Print statistics
print("Running Jobs Per User:")
for user, count in running_jobs_per_user.items():
  print(f"\t{user}: {count}")

print("\nPending Jobs Per User:")
for user, count in pending_jobs_per_user.items():
  print(f"\t{user}: {count}")

print("\nUsers Using the Most Nodes:")
running_max_users = get_user_with_max_nodes(max_nodes_per_user_running)
pending_max_users = get_user_with_max_nodes(max_nodes_per_user_pending)

print(f"\tRunning Jobs: {', '.join(running_max_users)} ({max_nodes_overall} nodes)")  
print(f"\tPending Jobs: {', '.join(pending_max_users)} ({max_nodes_overall} nodes)") 

print(f"\nMax Nodes Used Overall: {max_nodes_overall}") 

