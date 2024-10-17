import matplotlib.pyplot as plt

# Read the combined package list
with open('all_packages.txt', 'r') as file:
    packages = file.readlines()

package_names = [pkg.split()[0] for pkg in packages]  # Get package names only
counts = [1] * len(package_names)  # Count for each package (1)

plt.figure(figsize=(10, 8))
plt.barh(package_names, counts, color='skyblue')
plt.xlabel('Packages')
plt.title('Installed Packages')
plt.show()
