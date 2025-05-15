import matplotlib.pyplot as plt
import statistics

#data analysis
def analyze(data):
  total = 0.0
  minimum = data[0]
  maximum = data[0]
  for x in data:
    total += x
    if x < minimum:
      minimum = x
    if x > maximum:
      maximum = x
  mean = total / len(data)
  return mean, minimum, maximum

def main():
# 1.1 prompt the user
    data_str = input("Enter spike times (s), separated by spaces: ")
# 1.2 Split & convert
    spike_times = [float(t) for t in data_str.split()] #str.split()without arguments splits on any whitespace

    print("Spike times list:", spike_times)

#2.1 Initialize an empty list
    isis = []

#2.2 Loop through indices 0 to len(spike_times)-2
    for i in range(len(spike_times) - 1):
      interval = spike_times[i+1] - spike_times[i]
      isis.append(interval)

    print("Interspike intervals:", isis)
#analyze ISIs
    print("\n--- ISI Statistics ---")
    print(f"Mean ISI: {mean:.3f}s")
    print(f"Min ISI : {minimum:.3f}s")
    print(f"Max ISI : {maximum:.3f}s")

#firing rate
    num_spikes = len(spike_times)
    total_time = spike_times[-1] #time of the last spike
    firing_rate = num_spikes / total_time
    print(f"Firing rate: {firing_rate:.2f}Hz")

#Raster plot of spikes
    plt.figure(figsize=(6, 1))
    plt.eventplot(spike_times, lineoffsets=1)
    plt.xlim(0, spike_times[-1])
    plt.yticks([]) #hide y axis
    plt.xlabel("Time (s)")
    plt.title("Spike Raster Plot")
    plt.show()

#ISI Histogram
    plt.figure(figsize=(5, 4))
    plt.hist(isis, bins=10, edgecolor='black')
    plt.xlabel("Interspike Interval (s)")
    plt.ylabel("Count")
    plt.title("ISI Distribution")
    plt.show()

if __name__ == "__main__":
    main()


##Claude's improvements
import matplotlib.pyplot as plt
import statistics

# Data analysis function
def analyze(data):
    if not data:  # Handle empty list case
        return None, None, None
    
    total = sum(data)
    minimum = min(data)
    maximum = max(data)
    mean = total / len(data)
    return mean, minimum, maximum

def main():
    # 1.1 Prompt the user
    data_str = input("Enter spike times (s), separated by spaces: ")
    
    # 1.2 Split & convert
    try:
        spike_times = [float(t) for t in data_str.split()]  # str.split() without arguments splits on any whitespace
    except ValueError:
        print("Error: Please enter valid numeric values separated by spaces.")
        return
    
    if len(spike_times) < 2:
        print("Error: Need at least 2 spike times to calculate intervals.")
        return
        
    print("Spike times list:", spike_times)

    # 2.1 Initialize an empty list
    isis = []

    # 2.2 Loop through indices 0 to len(spike_times)-2
    for i in range(len(spike_times) - 1):
        interval = spike_times[i+1] - spike_times[i]
        isis.append(interval)

    print("Interspike intervals:", isis)
    
    # Analyze ISIs
    mean, minimum, maximum = analyze(isis)
    
    print("\n--- ISI Statistics ---")
    print(f"Mean ISI: {mean:.3f}s")
    print(f"Min ISI : {minimum:.3f}s")
    print(f"Max ISI : {maximum:.3f}s")
    print(f"Std Dev : {statistics.stdev(isis):.3f}s" if len(isis) > 1 else "Std Dev: N/A (need more data)")

    # Firing rate
    num_spikes = len(spike_times)
    total_time = spike_times[-1] - spike_times[0]  # Time from first to last spike
    firing_rate = (num_spikes - 1) / total_time if total_time > 0 else 0
    print(f"Firing rate: {firing_rate:.2f} Hz")

    # Raster plot of spikes
    plt.figure(figsize=(10, 2))
    plt.eventplot(spike_times, lineoffsets=1, linelengths=0.5, colors='black')
    plt.xlim(0, spike_times[-1] + 0.1)
    plt.yticks([])  # Hide y axis
    plt.xlabel("Time (s)")
    plt.title("Spike Raster Plot")
    plt.tight_layout()
    plt.show()

    # ISI Histogram
    plt.figure(figsize=(8, 5))
    bins = min(10, len(isis)) if isis else 10  # Adjust bin count based on data size
    plt.hist(isis, bins=bins, edgecolor='black', alpha=0.7)
    plt.axvline(mean, color='r', linestyle='dashed', linewidth=1, label=f'Mean: {mean:.3f}s')
    plt.xlabel("Interspike Interval (s)")
    plt.ylabel("Count")
    plt.title("ISI Distribution")
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
