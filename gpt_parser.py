def parse_log_file(log_file_path):
    # Initialize dictionaries to store user job counts, node usage, and nodes in use
    running_jobs_per_user = {}
    pending_jobs_per_user = {}
    node_usage_running = {}
    node_usage_pending = {}
    nodes_in_use_running = {}
    nodes_in_use_pending = {}

    with open(log_file_path, 'r') as file:
        for line in file:
            # Split line into components
            parts = line.split()
            if len(parts) < 8 or not parts[6].isdigit():
                continue  # Skip lines that don't match the expected format or don't have numeric NODES

            job_id, partition, name, user, status, _, nodes, _ = parts[:8]
            nodes = int(nodes)
            
            # Update counts and node usage for running jobs
            if status == 'R':
                running_jobs_per_user[user] = running_jobs_per_user.get(user, 0) + 1
                node_usage_running[user] = node_usage_running.get(user, 0) + nodes
                nodes_in_use_running[user] = nodes_in_use_running.get(user, 0) + 1
                
            # Update counts and node usage for pending jobs
            elif status == 'PD':
                pending_jobs_per_user[user] = pending_jobs_per_user.get(user, 0) + 1
                node_usage_pending[user] = node_usage_pending.get(user, 0) + nodes
                nodes_in_use_pending[user] = nodes_in_use_pending.get(user, 0) + 1

    # Calculate total node usage and nodes in use per user across running and pending jobs
    total_node_usage = {user: node_usage_running.get(user, 0) + node_usage_pending.get(user, 0) for user in set(node_usage_running) | set(node_usage_pending)}
    total_nodes_in_use = {user: nodes_in_use_running.get(user, 0) + nodes_in_use_pending.get(user, 0) for user in set(nodes_in_use_running) | set(nodes_in_use_pending)}

    return running_jobs_per_user, pending_jobs_per_user, node_usage_running, node_usage_pending, nodes_in_use_running, nodes_in_use_pending, total_node_usage, total_nodes_in_use

def print_statistics(running_jobs_per_user, pending_jobs_per_user, node_usage_running, node_usage_pending, nodes_in_use_running, nodes_in_use_pending, total_node_usage, total_nodes_in_use):
    # Find users using the most nodes for running, pending, and overall jobs
    users_most_nodes_running = max(node_usage_running, key=node_usage_running.get, default=None)
    users_most_nodes_pending = max(node_usage_pending, key=node_usage_pending.get, default=None)
    users_most_nodes_overall = max(total_node_usage, key=total_node_usage.get, default=None)

    # Print statistics
    print("Running Jobs per User:", running_jobs_per_user)
    print("Pending Jobs per User:", pending_jobs_per_user)
    print("Nodes in use for running jobs per user:", nodes_in_use_running)
    print("Nodes in use for pending jobs per user:", nodes_in_use_pending)
    print("Total nodes in use per user:", total_nodes_in_use)
    print("User with the most nodes for running jobs:", users_most_nodes_running)
    print("User with the most nodes for pending jobs:", users_most_nodes_pending)
    print("User with the most nodes overall:", users_most_nodes_overall)

# Example usage
log_file_path = 'log_file.txt'  # Assuming the log file is called log_file.txt
stats = parse_log_file(log_file_path)
print_statistics(*stats)

