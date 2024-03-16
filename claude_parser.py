from collections import defaultdict

# Initialize dictionaries to store job statistics
running_jobs_per_user = defaultdict(lambda: defaultdict(int))
pending_jobs_per_user = defaultdict(lambda: defaultdict(int))
running_nodes_per_user = defaultdict(int)
pending_nodes_per_user = defaultdict(int)
total_nodes_per_user = defaultdict(int)

# Open and parse the log file
with open("log_file.txt", "r") as file:
    # Skip the header line
    next(file)
    
    for line in file:
        # Split the line into fields
        fields = line.strip().split()
        
        # Extract relevant information
        user = fields[3]
        job_status = fields[4]
        nodes = int(fields[6])
        
        # Update job statistics based on job status
        if job_status == "R":
            running_jobs_per_user[user][nodes] += 1
            running_nodes_per_user[user] += nodes
        elif job_status == "PD":
            pending_jobs_per_user[user][nodes] += 1
            pending_nodes_per_user[user] += nodes
        
        # Update total nodes per user
        total_nodes_per_user[user] += nodes

# Print statistics
print("Running Jobs per User:")
for user, jobs_per_node in sorted(running_jobs_per_user.items(), key=lambda x: sum(k*v for k, v in x[1].items()), reverse=True):
    total_jobs = sum(jobs_per_node.values())
    total_nodes = sum(nodes * count for nodes, count in jobs_per_node.items())
    print(f"{user}: {total_jobs} (Nodes: {total_nodes})")

print("\nPending Jobs per User:")
for user, jobs_per_node in sorted(pending_jobs_per_user.items(), key=lambda x: sum(k*v for k, v in x[1].items()), reverse=True):
    total_jobs = sum(jobs_per_node.values())
    total_nodes = sum(nodes * count for nodes, count in jobs_per_node.items())
    print(f"{user}: {total_jobs} (Nodes: {total_nodes})")

print("\nUsers using the most nodes for Running Jobs:")
max_running_nodes_user = max(running_nodes_per_user, key=running_nodes_per_user.get)
max_running_nodes = running_nodes_per_user[max_running_nodes_user]
print(f"{max_running_nodes_user}: {max_running_nodes}")

print("\nUsers using the most nodes for Pending Jobs:")
max_pending_nodes_user = max(pending_nodes_per_user, key=pending_nodes_per_user.get)
max_pending_nodes = pending_nodes_per_user[max_pending_nodes_user]
print(f"{max_pending_nodes_user}: {max_pending_nodes}")

print("\nUsers using the most nodes Overall:")
max_total_nodes_user = max(total_nodes_per_user, key=total_nodes_per_user.get)
max_total_nodes = total_nodes_per_user[max_total_nodes_user]
print(f"{max_total_nodes_user}: {max_total_nodes}")

# Calculate total running nodes and total pending nodes
total_running_nodes = sum(running_nodes_per_user.values())
total_pending_nodes = sum(pending_nodes_per_user.values())

# Print total running nodes and total pending nodes
print("\nTotal Running Nodes:", total_running_nodes)
print("Total Pending Nodes:", total_pending_nodes)
