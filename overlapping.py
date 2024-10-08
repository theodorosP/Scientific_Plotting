import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde as kde
from matplotlib.colors import Normalize
from matplotlib import cm

# Function to calculate densities and colors for a given dataframe
def get_density_colours(df, column_name='size'):
    data = df[column_name].values
    densObj = kde(data)
    
    def make_colours(vals):
        norm = Normalize(vmin=vals.min(), vmax=vals.max())
        colours = [cm.ScalarMappable(norm=norm, cmap='jet').to_rgba(val) for val in vals]
        return colours
    
    densities = densObj(data)
    colours = make_colours(densities)
    
    return data, densities, colours

# Function to plot the data for the first dataframe
def plot_df1(df1, column_name='size'):
    data1, densities1, colours1 = get_density_colours(df1, column_name)

    plt.scatter(range(len(data1)), data1, color=colours1, label=f'{column_name} from df1')
    plt.xlabel('Index')
    plt.ylabel(column_name.capitalize())
    plt.title(f'{column_name.capitalize()} vs Index with Density Colors for df1')
    plt.legend()
    plt.show()

# Function to plot the data for the second dataframe
def plot_df2(df2, column_name='size'):
    data2, densities2, colours2 = get_density_colours(df2, column_name)

    plt.scatter(range(len(data2)), data2, color=colours2, label=f'{column_name} from df2')
    plt.xlabel('Index')
    plt.ylabel(column_name.capitalize())
    plt.title(f'{column_name.capitalize()} vs Index with Density Colors for df2')
    plt.legend()
    plt.show()

# Create two sample dataframes for testing
np.random.seed(0)
df1 = pd.DataFrame({
    'size': np.random.normal(loc=50, scale=10, size=1000)
})

np.random.seed(1)
df2 = pd.DataFrame({
    'size': np.random.normal(loc=50, scale=10, size=1000)
})

# Test the functions
plot_df1(df1)
plot_df2(df2)



--------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde as kde
from matplotlib.colors import Normalize
from matplotlib import cm

# Function to calculate densities and colors for a given dataframe
def get_density_colours(df, column_name='size'):
    data = df[column_name].values
    densObj = kde(data)
    
    def make_colours(vals):
        norm = Normalize(vmin=vals.min(), vmax=vals.max())
        colours = [cm.ScalarMappable(norm=norm, cmap='Blues').to_rgba(val) for val in vals]
        return colours
    
    densities = densObj(data)
    colours = make_colours(densities)
    
    return data, densities, colours

# Function to plot the data for the first dataframe
def plot_df1(df1, column_name='size'):
    data1, densities1, colours1 = get_density_colours(df1, column_name)

    plt.scatter(range(len(data1)), data1, color=colours1, label=f'{column_name} from df1')
    plt.xlabel('Index')
    plt.ylabel(column_name.capitalize())
    plt.title(f'{column_name.capitalize()} vs Index with Density Colors for df1')
    plt.legend()
    plt.show()

# Function to plot the data for the second dataframe
def plot_df2(df2, column_name='size'):
    data2, densities2, colours2 = get_density_colours(df2, column_name)

    plt.scatter(range(len(data2)), data2, color=colours2, label=f'{column_name} from df2')
    plt.xlabel('Index')
    plt.ylabel(column_name.capitalize())
    plt.title(f'{column_name.capitalize()} vs Index with Density Colors for df2')
    plt.legend()
    plt.show()

# Create two sample dataframes for testing
np.random.seed(0)
df1 = pd.DataFrame({
    'size': np.random.normal(loc=50, scale=10, size=1000)
})

np.random.seed(1)
df2 = pd.DataFrame({
    'size': np.random.normal(loc=50, scale=10, size=1000)
})

# Test the functions
plot_df1(df1)
plot_df2(df2)


-----------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde as kde
from matplotlib.colors import Normalize
from matplotlib import cm

# Function to calculate densities and colors for a given dataframe
def get_density_colours(df, column_name='size', cmap='Blues'):
    data = df[column_name].values
    densObj = kde(data)
    
    def make_colours(vals):
        norm = Normalize(vmin=vals.min(), vmax=vals.max())
        colours = [cm.ScalarMappable(norm=norm, cmap=cmap).to_rgba(val) for val in vals]
        return colours
    
    densities = densObj(data)
    colours = make_colours(densities)
    
    return data, densities, colours

# Function to plot the data for the first dataframe
def plot_df1(df1, column_name='size'):
    data1, densities1, colours1 = get_density_colours(df1, column_name, cmap='Blues')

    plt.scatter(range(len(data1)), data1, color=colours1, label=f'{column_name} from df1')
    plt.xlabel('Index')
    plt.ylabel(column_name.capitalize())
    plt.title(f'{column_name.capitalize()} vs Index with Density Colors for df1')
    plt.legend()
    plt.show()

# Function to plot the data for the second dataframe
def plot_df2(df2, column_name='size'):
    data2, densities2, colours2 = get_density_colours(df2, column_name, cmap='Greens')

    plt.scatter(range(len(data2)), data2, color=colours2, label=f'{column_name} from df2')
    plt.xlabel('Index')
    plt.ylabel(column_name.capitalize())
    plt.title(f'{column_name.capitalize()} vs Index with Density Colors for df2')
    plt.legend()
    plt.show()

# Create two sample dataframes for testing
np.random.seed(0)
df1 = pd.DataFrame({
    'size': np.random.normal(loc=50, scale=10, size=1000)
})

np.random.seed(1)
df2 = pd.DataFrame({
    'size': np.random.normal(loc=50, scale=10, size=1000)
})

# Test the functions
plot_df1(df1)
plot_df2(df2)

-------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde as kde
from matplotlib.colors import Normalize
from matplotlib import cm

# Function to calculate densities and colors for a given dataframe
def get_density_colours(df, column_name='size', cmap='Blues'):
    data = df[column_name].values
    densObj = kde(data)
    
    def make_colours(vals):
        norm = Normalize(vmin=vals.min(), vmax=vals.max())
        colours = [cm.ScalarMappable(norm=norm, cmap=cmap).to_rgba(val) for val in vals]
        return colours
    
    densities = densObj(data)
    colours = make_colours(densities)
    
    return data, densities, colours

# Function to plot both dataframes together
def plot_combined_density(df1, df2, column_name='size'):
    data1, densities1, colours1 = get_density_colours(df1, column_name, cmap='Blues')
    data2, densities2, colours2 = get_density_colours(df2, column_name, cmap='Greens')
    
    plt.figure(figsize=(10, 6))
    
    # Plot data for df1
    plt.scatter(range(len(data1)), data1, color=colours1, label=f'{column_name} from df1')
    
    # Plot data for df2
    plt.scatter(range(len(data2)), data2, color=colours2, label=f'{column_name} from df2')

    # Identify overlapping points and plot them in yellow
    combined_indices = range(len(data1) + len(data2))
    combined_data = np.concatenate((data1, data2))
    combined_kde = kde(combined_data)
    combined_densities = combined_kde(combined_data)
    combined_norm = Normalize(vmin=combined_densities.min(), vmax=combined_densities.max())
    yellow_colours = [cm.ScalarMappable(norm=combined_norm, cmap='YlOrRd').to_rgba(val) for val in combined_densities]

    plt.scatter(combined_indices, combined_data, color=yellow_colours, label='Overlapping points', alpha=0.6)

    plt.xlabel('Index')
    plt.ylabel(column_name.capitalize())
    plt.title(f'{column_name.capitalize()} vs Index with Density Colors')
    plt.legend()
    plt.show()

# Create two sample dataframes for testing
np.random.seed(0)
df1 = pd.DataFrame({
    'size': np.random.normal(loc=50, scale=10, size=1000)
})

np.random.seed(1)
df2 = pd.DataFrame({
    'size': np.random.normal(loc=50, scale=10, size=1000)
})

# Test the function
plot_combined_density(df1, df2)
---------------

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde as kde
from matplotlib.colors import Normalize
from matplotlib import cm

# Function to calculate densities for a given dataframe
def get_density(df, column_name='size'):
    data = df[column_name].values
    densObj = kde(data)
    densities = densObj(data)
    return data, densities

# Function to plot both dataframes together with seaborn
def plot_combined_density(df1, df2, column_name='size'):
    data1, densities1 = get_density(df1, column_name)
    data2, densities2 = get_density(df2, column_name)
    
    # Normalize densities for color mapping
    norm1 = Normalize(vmin=densities1.min(), vmax=densities1.max())
    norm2 = Normalize(vmin=densities2.min(), vmax=densities2.max())
    
    colors1 = [cm.ScalarMappable(norm=norm1, cmap='Blues').to_rgba(val) for val in densities1]
    colors2 = [cm.ScalarMappable(norm=norm2, cmap='Greens').to_rgba(val) for val in densities2]
    
    plt.figure(figsize=(14, 8))
    
    # Scatter plot for df1
    sns.scatterplot(x=range(len(data1)), y=data1, hue=densities1, palette='Blues', legend=False, alpha=0.6)
    
    # Scatter plot for df2
    sns.scatterplot(x=range(len(data2)), y=data2, hue=densities2, palette='Greens', legend=False, alpha=0.6)
    
    # Combine data for overlap
    combined_data = np.concatenate((data1, data2))
    combined_indices = range(len(combined_data))
    combined_kde = kde(combined_data)
    combined_densities = combined_kde(combined_data)
    combined_norm = Normalize(vmin=combined_densities.min(), vmax=combined_densities.max())
    yellow_colours = [cm.ScalarMappable(norm=combined_norm, cmap='YlOrRd').to_rgba(val) for val in combined_densities]
    
    # Plot combined data with yellow color for overlapping points
    plt.scatter(combined_indices, combined_data, color=yellow_colours, label='Overlapping points', alpha=0.3)

    plt.xlabel('Index')
    plt.ylabel(column_name.capitalize())
    plt.title(f'{column_name.capitalize()} vs Index with Density Colors')
    plt.legend()
    plt.show()

# Create two sample dataframes for testing with larger dataset
np.random.seed(0)
df1 = pd.DataFrame({
    'size': np.random.normal(loc=50, scale=10, size=2000000)
})

np.random.seed(1)
df2 = pd.DataFrame({
    'size': np.random.normal(loc=50, scale=10, size=2000000)
})

# Test the function
plot_combined_density(df1, df2)

-------------

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde as kde
from matplotlib.colors import Normalize
from matplotlib import cm

# Function to calculate densities and colors for a given dataframe
def get_density_colours(df, column_name='size', cmap='Blues'):
    data = df[column_name].values
    densObj = kde(data)

    def make_colours(vals):
        norm = Normalize(vmin=vals.min(), vmax=vals.max())
        colours = [cm.ScalarMappable(norm=norm, cmap=cmap).to_rgba(val) for val in vals]
        return colours

    densities = densObj(data)
    colours = make_colours(densities)

    return data, densities, colours

# Function to plot both dataframes together using seaborn
def plot_combined_density(df1, df2, column_name='size'):
    data1, densities1, colours1 = get_density_colours(df1, column_name, cmap='Blues')
    data2, densities2, colours2 = get_density_colours(df2, column_name, cmap='Greens')

    # Combine data and densities
    combined_data = np.concatenate((data1, data2))
    combined_densities = np.concatenate((densities1, densities2))

    # Create a DataFrame to store combined data and densities
    df_combined = pd.DataFrame({
        'Index': np.arange(len(combined_data)),
        'Size': combined_data,
        'Density': combined_densities
    })

    # Plot using seaborn scatterplot with alpha blending for overlapping points
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df_combined, x='Index', y='Size', hue='Density', palette='YlOrRd', alpha=0.6)
    
    plt.xlabel('Index')
    plt.ylabel(column_name.capitalize())
    plt.title(f'{column_name.capitalize()} vs Index with Density Colors')
    plt.legend()
    plt.tight_layout()
    plt.show()

# Create two sample dataframes for testing
np.random.seed(0)
df1 = pd.DataFrame({
    'size': np.random.normal(loc=50, scale=10, size=1000)
})

np.random.seed(1)
df2 = pd.DataFrame({
    'size': np.random.normal(loc=50, scale=10, size=1000)
})

# Test the function
plot_combined_density(df1, df2)

---

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde as kde
from matplotlib.colors import LinearSegmentedColormap, Normalize
from matplotlib import cm

# Function to create a custom colormap with lighter shades of blue
def create_light_blue_colormap():
    colors = [(0.9, 0.9, 1.0), (0.6, 0.6, 1.0), (0.3, 0.3, 1.0), (0.0, 0.0, 0.8)]  # Light to dark blue
    cmap = LinearSegmentedColormap.from_list('custom_light_blue', colors)
    return cmap

# Function to calculate densities for a given dataframe
def get_density(df, column_name='size'):
    data = df[column_name].values
    densObj = kde(data)
    densities = densObj(data)
    return data, densities

# Function to plot data from both dataframes separately
def plot_density(df1, df2, column_name='size'):
    data1, densities1 = get_density(df1, column_name)
    data2, densities2 = get_density(df2, column_name)
    
    # Normalize densities for each dataframe
    norm1 = Normalize(vmin=densities1.min(), vmax=densities1.max())
    norm2 = Normalize(vmin=densities2.min(), vmax=densities2.max())
    
    # Generate colors based on normalized densities
    colors1 = [cm.ScalarMappable(norm=norm1, cmap=create_light_blue_colormap()).to_rgba(val) for val in densities1]
    colors2 = [cm.ScalarMappable(norm=norm2, cmap='Greens').to_rgba(val) for val in densities2]
    
    plt.figure(figsize=(14, 8))
    
    # Scatter plot for df1 with custom light blue colormap
    sns.scatterplot(x=range(len(data1)), y=data1, hue=densities1, palette=create_light_blue_colormap(), legend=False, alpha=0.6)
    
    # Scatter plot for df2 with light green to green gradient
    sns.scatterplot(x=range(len(data1), len(data1) + len(data2)), y=data2, hue=densities2, palette='Greens', legend=False, alpha=0.6)

    plt.xlabel('Index')
    plt.ylabel(column_name.capitalize())
    plt.title(f'{column_name.capitalize()} vs Index with Density Colors')
    plt.legend()
    plt.show()

# Create two sample dataframes for testing
np.random.seed(0)
df1 = pd.DataFrame({
    'size': np.random.normal(loc=50, scale=10, size=2000000)
})

np.random.seed(1)
df2 = pd.DataFrame({
    'size': np.random.normal(loc=50, scale=10, size=2000000)
})

# Test the function
plot_density(df1, df2)




def create_light_green_colormap():
    colors = [(0.9, 1.0, 0.9), (0.6, 1.0, 0.6), (0.3, 1.0, 0.3), (0.0, 0.8, 0.0)]  # Light to dark green
    cmap = LinearSegmentedColormap.from_list('custom_light_green', colors)
    return cmap


-----------------

def process_file(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    new_lines = []
    
    for line in lines:
        new_lines.append(line.strip())  # Original line
        words = line.strip().split()
        if words[0].endswith('_a'):
            number = int(''.join(filter(str.isdigit, words[0])))
            half_number = number / 2
            if len(words) > 4:  # Ensure there are at least 5 words
                words[2] = str(float(words[2]) + half_number)
                words[4] = str(float(words[4]) + half_number)
                new_line = ' '.join(words)
                new_lines.append(new_line)

    with open(output_file, 'w') as f:
        for line in new_lines:
            f.write(line + '\n')

# Usage example
input_file = 'input.txt'
output_file = 'output.txt'
process_file(input_file, output_file)


-------------

def process_file(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    new_lines = []
    
    for line in lines:
        new_lines.append(line.strip())  # Original line
        words = line.strip().split()
        if words[0].endswith('_a'):
            number = int(''.join(filter(str.isdigit, words[0])))
            half_number = number / 2
            if len(words) > 4:  # Ensure there are at least 5 words
                words[2] = str(float(words[2]) + half_number)
                words[4] = str(float(words[4]) + half_number)
                words[0] = words[0][:-1] + 'c'  # Change '_a' to '_c' in the first word
                new_line = ' '.join(words)
                new_lines.append(new_line)

    with open(output_file, 'w') as f:
        for line in new_lines:
            f.write(line + '\n')

# Usage example
input_file = 'input.txt'
output_file = 'output.txt'
process_file(input_file, output_file)

------

def process_file(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    new_lines = []

    for line in lines:
        new_lines.append(line.rstrip())  # Original line with its original spacing
        words = line.split()
        if words and words[0].endswith('_a'):
            # Extract number from the first word
            number = int(''.join(filter(str.isdigit, words[0])))
            half_number = number / 2
            new_words = words.copy()
            
            # Modify the third and fifth words
            if len(new_words) > 4:
                new_words[2] = str(float(new_words[2]) + half_number)
                new_words[4] = str(float(new_words[4]) + half_number)
                new_words[0] = new_words[0][:-1] + 'c'  # Change '_a' to '_c' in the first word

            # Construct the new line with the same spacing as the original line
            new_line = line.replace(words[0], new_words[0], 1)
            new_line = new_line.replace(words[2], new_words[2], 1)
            new_line = new_line.replace(words[4], new_words[4], 1)

            new_lines.append(new_line.rstrip())

    with open(output_file, 'w') as f:
        for line in new_lines:
            f.write(line + '\n')

# Usage example
input_file = 'input.txt'
output_file = 'output.txt'
process_file(input_file, output_file)

------

def process_file(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    new_lines = []

    for line in lines:
        new_lines.append(line.rstrip())  # Original line with its original spacing
        words = line.split()
        if words and words[0].endswith('_a'):
            # Extract number from the first word
            number_str = ''.join(filter(str.isdigit, words[0]))
            number = int(number_str) if number_str else 0
            half_number = number / 2.0
            
            if len(words) > 4:
                # Preserve original spacing
                prefix = line.split(words[0])[0]
                space_between_first_and_third = line.split(words[2])[0].split(words[0])[1]
                space_between_third_and_fifth = line.split(words[4])[0].split(words[2])[1]

                new_first_word = words[0][:-1] + 'c'
                new_third_word = str(float(words[2]) + half_number)
                new_fifth_word = str(float(words[4]) + half_number)
                
                new_line = prefix + new_first_word + space_between_first_and_third + new_third_word + space_between_third_and_fifth + new_fifth_word
                new_lines.append(new_line.rstrip())

    with open(output_file, 'w') as f:
        for line in new_lines:
            f.write(line + '\n')

# Usage example
input_file = 'input.txt'
output_file = 'output.txt'
process_file(input_file, output_file)


_____

def process_file(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    new_lines = []

    for line in lines:
        new_lines.append(line.rstrip())  # Add original line
        words = line.split()
        if words and words[0].endswith('_a'):
            # Extract number from the first word
            number_str = ''.join(filter(str.isdigit, words[0]))
            number = int(number_str) if number_str else 0
            half_number = number / 2.0

            # Create a new list of words for the modified line
            new_words = words[:]
            new_words[0] = words[0][:-1] + 'c'
            if len(words) > 4:
                try:
                    new_words[2] = str(float(words[2]) + half_number)
                    new_words[4] = str(float(words[4]) + half_number)
                except ValueError:
                    # In case the 3rd and 5th words are not numbers, skip them
                    pass
            
            # Reconstruct the line while preserving original spacing
            index1 = line.find(words[0])
            index2 = line.find(words[2], index1 + len(words[0]))
            index3 = line.find(words[4], index2 + len(words[2]))
            
            new_line = (line[:index1] + new_words[0] +
                        line[index1 + len(words[0]):index2] + new_words[2] +
                        line[index2 + len(words[2]):index3] + new_words[4] +
                        line[index3 + len(words[4]):])
            
            new_lines.append(new_line.rstrip())

    with open(output_file, 'w') as f:
        for line in new_lines:
            f.write(line + '\n')

# Usage example
input_file = 'input.txt'
output_file = 'output.txt'
process_file(input_file, output_file)

____

def process_file(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    new_lines = []

    for line in lines:
        new_lines.append(line.rstrip())  # Add original line
        words = line.split()
        if words and words[0].endswith('_a'):
            # Extract number from the first word
            number_str = ''.join(filter(str.isdigit, words[0]))
            number = int(number_str) if number_str else 0
            half_number = number / 2.0

            # Create a new list of words for the modified line
            new_words = words[:]
            new_words[0] = words[0][:-1] + 'c'
            if len(words) > 5:
                try:
                    new_words[3] = str(float(words[3]) + half_number)
                    new_words[5] = str(float(words[5]) + half_number)
                except ValueError:
                    # In case the 4th and 6th words are not numbers, skip them
                    pass
            
            # Reconstruct the line while preserving original spacing
            index1 = line.find(words[0])
            index2 = line.find(words[3], index1 + len(words[0]))
            index3 = line.find(words[5], index2 + len(words[3]))
            
            new_line = (line[:index1] + new_words[0] +
                        line[index1 + len(words[0]):index2] + new_words[3] +
                        line[index2 + len(words[3]):index3] + new_words[5] +
                        line[index3 + len(words[5]):])
            
            new_lines.append(new_line.rstrip())

    with open(output_file, 'w') as f:
        for line in new_lines:
            f.write(line + '\n')

# Usage example
input_file = 'input.txt'
output_file = 'output.txt'
process_file(input_file, output_file)

----

def count_lines(file_path):
    with open(file_path, 'r') as file:
        line_count = sum(1 for _ in file)
    return line_count

# Usage
file_path = 'path/to/your/large_file.txt'
number_of_lines = count_lines(file_path)
print(f"The file has {number_of_lines} lines.")


---

#!/bin/bash

# Initialize the total sum variable
total_sum=0

# Iterate over all files in the directory
for file in *; do
  if [[ -f $file ]]; then
    # Sum numbers on lines starting with 'ptablel_after' in the current file
    file_sum=$(grep '^ptablel_after' "$file" | awk '{sum += $2} END {print sum}')
    
    # Add the file sum to the total sum
    total_sum=$((total_sum + file_sum))
  fi
done

# Print the total sum
echo "Total sum: $total_sum"

----

#!/bin/bash

# Initialize the total sum variable
total_sum=0

# Iterate over all files in the directory
for file in *; do
  if [[ -f $file ]]; then
    # Extract lines starting with 'ptablel_after' and sum the numbers in the second column
    file_sum=$(grep '^ptablel_after' "$file" | awk '{sum += $2} END {if (NR > 0) print sum; else print 0}')
    
    # Add the file sum to the total sum
    total_sum=$((total_sum + file_sum))
  fi
done

# Print the total sum
echo "Total sum: $total_sum"

___

#!/bin/bash

# Initialize the total sum variable
total_sum=0

# Iterate over all files in the directory
for file in *; do
  if [[ -f $file ]]; then
    # Extract lines starting with 'ptablel_after', get the second column, and sum the numbers
    file_sum=$(grep '^ptablel_after' "$file" | awk '{sum += $2} END {print sum}')
    
    # Ensure file_sum is not empty
    if [ -n "$file_sum" ]; then
      total_sum=$(echo "$total_sum + $file_sum" | bc)
    fi
  fi
done

# Print the total sum
echo "Total sum: $total_sum"

---

#!/bin/bash

# Initialize the total sum variable
total_sum=0

# Iterate over all files with names starting with 'ptablel_after'
for file in ptablel_after*; do
  if [[ -f $file ]]; then
    # Sum all numbers in the file
    file_sum=$(awk '{sum += $1} END {print sum}' "$file")
    
    # Ensure file_sum is not empty
    if [ -n "$file_sum" ]; then
      total_sum=$(echo "$total_sum + $file_sum" | bc)
    fi
  fi
done

# Print the total sum
echo "Total sum: $total_sum"

___

#!/bin/bash

average_sixth_column() {
  for file in Rep_*; do
    if [[ -f $file ]]; then
      awk '/^id/ {sum += $6; count++} END {if (count > 0) print FILENAME, sum/count}' "$file"
    fi
  done
}

# Call the function
average_sixth_column


___

#!/bin/bash

# Read the file line by line
while IFS= read -r line; do
  # Get the first word of the line
  first_word=$(echo $line | awk '{print $1}')
  
  # Check if the first word is 'id'
  if [ "$first_word" == "id" ]; then
    # Print the line if the first word is 'id'
    echo $line
  fi
done < Rep_01.txt



___

#!/bin/bash

file_path="Rep_01.txt"

# Initialize variables for sum and count
sum=0
count=0

# Read the file line by line
while IFS= read -r line; do
  # Get the first word of the line
  first_word=$(echo "$line" | awk '{print $1}')
  
  # Check if the first word is 'id'
  if [ "$first_word" == "id" ]; then
    # Extract the sixth column value
    sixth_column=$(echo "$line" | awk '{print $6}')
    
    # Check if sixth column value is numeric
    if [[ "$sixth_column" =~ ^[0-9]+(\.[0-9]+)?$ ]]; then
      # Add to sum and increment count
      sum=$(awk "BEGIN {print $sum + $sixth_column}")
      (( count++ ))
    fi
  fi
done < "$file_path"

# Calculate the average
if [ $count -gt 0 ]; then
  average=$(awk "BEGIN {print $sum / $count}")
  echo "Average of the sixth column: $average"
else
  echo "No lines with 'id' found or sixth column values are missing or not numeric."
fi


___

#!/bin/bash

file_path="Rep_01.txt"

# Initialize variables for sum and count
sum=0
count=0

# Read the file line by line
while IFS= read -r line; do
  # Get the first word of the line
  first_word=$(echo "$line" | awk '{print $1}')
  
  # Check if the first word is 'id'
  if [ "$first_word" == "id" ]; then
    # Extract the sixth column value
    sixth_column=$(echo "$line" | awk '{print $6}')
    
    # Check if sixth column value is numeric
    if [[ "$sixth_column" =~ ^-?[0-9]+(\.[0-9]+)?$ ]]; then
      # Convert negative values to positive
      if (( $(echo "$sixth_column < 0" | bc -l) )); then
        sixth_column=$(echo "$sixth_column * -1" | bc)
      fi
      
      # Add to sum and increment count
      sum=$(awk "BEGIN {print $sum + $sixth_column}")
      (( count++ ))
    fi
  fi
done < "$file_path"

# Calculate the average
if [ $count -gt 0 ]; then
  average=$(awk "BEGIN {print $sum / $count}")
  echo "Average of the sixth column: $average"
else
  echo "No lines with 'id' found or sixth column values are missing or not numeric."
fi

___

#!/bin/bash

# Directory where Rep_ files are located
directory="/path/to/directory"

# Initialize variables for sum and count
total_sum=0
total_count=0
file_count=0

# Loop through each file starting with "Rep_" in the directory
for file_path in "$directory"/Rep_*; do
  # Check if file exists and is readable
  if [ -f "$file_path" ] && [ -r "$file_path" ]; then
    # Increment file count
    (( file_count++ ))
    
    # Process each file line by line
    while IFS= read -r line; do
      # Get the first word of the line
      first_word=$(echo "$line" | awk '{print $1}')
      
      # Check if the first word is 'id'
      if [ "$first_word" == "id" ]; then
        # Extract the sixth column value
        sixth_column=$(echo "$line" | awk '{print $6}')
        
        # Check if sixth column value is numeric
        if [[ "$sixth_column" =~ ^-?[0-9]+(\.[0-9]+)?$ ]]; then
          # Convert negative values to positive
          if (( $(echo "$sixth_column < 0" | bc -l) )); then
            sixth_column=$(echo "$sixth_column * -1" | bc)
          fi
          
          # Add to total sum and increment total count
          total_sum=$(awk "BEGIN {print $total_sum + $sixth_column}")
          (( total_count++ ))
        fi
      fi
    done < "$file_path"
  else
    echo "Error: File $file_path not found or not readable."
  fi
done

# Calculate the average across all files
if [ $total_count -gt 0 ]; then
  average=$(awk "BEGIN {print $total_sum / $total_count}")
  echo "Average of the sixth column across $file_count files: $average"
else
  echo "No valid lines with 'id' found across files or sixth column values are missing or not numeric."
fi


___

#!/bin/bash

# Directory where Rep_ files are located
directory="/path/to/directory"

# Initialize variables for sum and count
file_count=0

# Loop through each file starting with "Rep_" in the directory
for file_path in "$directory"/Rep_*; do
  # Check if file exists and is readable
  if [ -f "$file_path" ] && [ -r "$file_path" ]; then
    # Increment file count
    (( file_count++ ))
    
    # Initialize variables for current file
    sum=0
    count=0
    
    # Process each file line by line
    while IFS= read -r line; do
      # Get the first word of the line
      first_word=$(echo "$line" | awk '{print $1}')
      
      # Check if the first word is 'id'
      if [ "$first_word" == "id" ]; then
        # Extract the sixth column value
        sixth_column=$(echo "$line" | awk '{print $6}')
        
        # Check if sixth column value is numeric
        if [[ "$sixth_column" =~ ^-?[0-9]+(\.[0-9]+)?$ ]]; then
          # Convert negative values to positive
          if (( $(echo "$sixth_column < 0" | bc -l) )); then
            sixth_column=$(echo "$sixth_column * -1" | bc)
          fi
          
          # Add to sum and increment count
          sum=$(awk "BEGIN {print $sum + $sixth_column}")
          (( count++ ))
        fi
      fi
    done < "$file_path"
    
    # Calculate the average for the current file
    if [ $count -gt 0 ]; then
      average=$(awk "BEGIN {print $sum / $count}")
      echo "Average of sixth column in file $(basename "$file_path"): $average"
    else
      echo "No valid lines with 'id' found in file $(basename "$file_path") or sixth column values are missing or not numeric."
    fi
    
  else
    echo "Error: File $file_path not found or not readable."
  fi
done


___

import matplotlib.pyplot as plt
import seaborn as sns

# Example list of values
data = [10, 20, 15, 35, 45, 55, 65, 75, 85, 95, 25, 35, 45, 55, 60, 70, 80, 90, 100, 110]

# Create a figure and axis
fig, ax = plt.subplots()

# Create a box plot
sns.boxplot(data=data, ax=ax)

# Overlay a strip plot to show each individual data point
sns.stripplot(data=data, ax=ax, color='red', jitter=True)

# Add title and labels
ax.set_title('Box Plot with Individual Data Points')
ax.set_ylabel('Values')

# Display the plot
plt.show()


___

class table:
    def __init__(self):
        self.data = [1, 2, 3]
        self.name = "Sample Table"
    
    def get_data(self):
        return self.data
    
    def get_name(self):
        return self.name
    
    def get_summary(self):
        return f"Table: {self.name}, Data: {self.data}"

# Create an instance of the table class
table_instance = table()


___

import pandas as pd

# Sample DataFrame
data = {
    'col1': [1, 2, 3],
    'col2': [4, 5, 6],
    'col3': [7, 8, 9],
    'col4': [10, 11, 12]
}
df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Get the current name of the second column (index 1 in zero-based indexing)
original_col_name = df.columns[1]

# Rename the second column to 'ils'
df.rename(columns={original_col_name: 'ils'}, inplace=True)

# Display the modified DataFrame
print("\nModified DataFrame (second column renamed to 'ils'):")
print(df)


___

import pandas as pd
import numpy as np

# Example DataFrames
df1 = pd.DataFrame({
    'gauge': ['A', 'B', 'C', 'D'],
    'AI_CD': [10, 20, 30, 40]
})

df2 = pd.DataFrame({
    'gauge': ['A', 'B', 'X', 'D'],
    'AI_CD': [15, 25, 35, 45]
})

# Merge the two DataFrames on the 'gauge' column
merged_df = pd.merge(df1, df2, on='gauge', how='outer', suffixes=('_df1', '_df2'))

# Compute the absolute difference where the 'gauge' names are the same in both DataFrames
merged_df['AI_CD_diff'] = np.where(merged_df[['AI_CD_df1', 'AI_CD_df2']].notna().all(axis=1), 
                                    abs(merged_df['AI_CD_df1'] - merged_df['AI_CD_df2']), 
                                    np.nan)

# Select only the necessary columns for the final DataFrame
final_df = merged_df[['gauge', 'AI_CD_diff']]

print(final_df)


___

import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'gauge_temp': [1, 2, 3],
    'gauge_pressure': [4, 5, 6],
    'ils_speed': [7, 8, 9],
    'AI_CD_quality': [10, 11, 12],
    'other_column': [13, 14, 15]
})

# List of column names to keep
columns_to_keep = ['gauge_temp', 'gauge_pressure', 'ils_speed', 'AI_CD_quality']

# Keep columns that are in the list or start with specific prefixes
filtered_df = df[[col for col in df.columns if col in columns_to_keep or col.startswith('gauge') or col.startswith('ils') or col.startswith('AI_CD')]]

print(filtered_df)

___

import matplotlib.pyplot as plt

# Create a figure and an axes
fig, ax = plt.subplots()

# Plot a horizontal line at y=0.2 with a light grey color
ax.axhline(y=0.2, color='grey', linestyle='--', linewidth=1)

# Add a label to the line
ax.text(0.5, 0.2, 'Threshold = 0.2', color='grey', fontsize=12, ha='center', va='bottom', backgroundcolor='w')

# Optionally, plot some data for context
x = [0, 1, 2, 3, 4, 5]
y = [0.1, 0.3, 0.15, 0.25, 0.18, 0.22]
ax.plot(x, y, marker='o')

# Set labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Plot with Horizontal Line at y=0.2')

# Show the plot
plt.show()


___

Geometrical corner rounding in computational lithography is crucial for maintaining pattern fidelity in semiconductor manufacturing. This poster introduces an optimized method that achieves a 20% reduction in simulation run time while preserving accuracy, significantly improving computational efficiency and resolution.


Corner rounding in lithography is caused by the diffraction of light and imperfections in the photomask and exposure processes. This phenomenon leads to deviations from the intended pattern, impacting the accuracy of semiconductor manufacturing.

In simulations, these rounding effects must be accurately modeled to predict and correct pattern distortions. However, current approaches often lack optimal simulation values and can waste significant computational resources.

This poster introduces a new method that reduces simulation run time by 20% while preserving accuracy, enhancing computational efficiency and addressing the inefficiencies in modeling geometrical corner rounding.


Corner rounding in lithography arises from light diffraction and photomask imperfections, causing deviations from intended patterns.

Accurate simulation of these effects is crucial but often inefficient, leading to excessive computational time.

This poster presents a method that reduces simulation run time by 20% while maintaining accuracy, improving efficiency in modeling corner rounding.


___

import matplotlib.pyplot as plt
import pandas as pd

# Example dictionary S with dataframes (assuming you have the actual dataframes)
# S = {'TCC_1': df1, 'TCC_2': df2, ..., 'TCC_24': df24}

# Extract the maximum values for each dataframe
max_values = {key: df['AI_CD_diff'].max() for key, df in S.items()}

# Combine all dataframes for the box plot
combined_df = pd.concat(S.values(), keys=S.keys()).reset_index(level=0).rename(columns={'level_0': 'Category'})

# Initialize the plot and axes
fig, ax = plt.subplots(figsize=(14, 8))

# Create the box plot for each key in the dictionary
categories = list(S.keys())
data = [S[key]['AI_CD_diff'] for key in categories]

# Plot the box plots
boxprops = dict(facecolor='lightblue', color='black')
ax.boxplot(data, positions=range(len(categories)), patch_artist=True, boxprops=boxprops)

# Plot the maximum values as red dots
for i, key in enumerate(categories):
    ax.plot(i + 1, max_values[key], 'ro', label=f'Max {key}' if i == 0 else "")

# Set the x-ticks and labels
ax.set_xticks(range(1, len(categories) + 1))
ax.set_xticklabels(categories, rotation=45)
ax.set_xlabel('Category')
ax.set_ylabel('AI_CD_diff')
ax.set_title('Box Plot and Max Values of AI_CD_diff')

# Add a legend
ax.legend()

# Adjust layout
plt.tight_layout()
plt.show()


----------------------------

import matplotlib.pyplot as plt

# Example dictionary with 10 dataframes
dfs = {
    'df1': df1,
    'df2': df2,
    'df3': df3,
    'df4': df4,
    'df5': df5,
    'df6': df6,
    'df7': df7,
    'df8': df8,
    'df9': df9,
    'df10': df10
}

# Create a figure and axis for the box plots
plt.figure(figsize=(12, 8))

# Iterate over the dictionary and create a box plot for the AI_CD_diff column of each dataframe
for i, (key, df) in enumerate(dfs.items(), start=1):
    # Extract the AI_CD_diff column
    data = df['AI_CD_diff']
    
    # Plot each dataframe's AI_CD_diff column as a boxplot on the same axis
    plt.boxplot(data, positions=[i], widths=0.5, patch_artist=True)

# Add titles and labels
plt.title('Box Plots for AI_CD_diff Column in All DataFrames')
plt.xlabel('DataFrame Index')
plt.ylabel('AI_CD_diff Values')

# Customize x-axis ticks to match DataFrame names
plt.xticks(range(1, len(dfs) + 1), [key for key in dfs.keys()])

# Show the plot
plt.show()


___

import pandas as pd

# Assuming df is your dataframe
max_row = df.loc[df['AI_CD_diff'].idxmax()]

# Extract the maximum AI_CD_diff and corresponding gauge value
max_ai_cd_diff = max_row['AI_CD_diff']
corresponding_gauge = max_row['gauges']

print("Maximum AI_CD_diff:", max_ai_cd_diff)
print("Corresponding gauge value:", corresponding_gauge)

___

import pandas as pd

# Assuming df is your dataframe
max_index = df['AI_CD_diff'].idxmax()
max_row = df.loc[max_index]

# Extract the maximum AI_CD_diff and corresponding gauge value
max_ai_cd_diff = max_row['AI_CD_diff']
corresponding_gauge = max_row['gauges']

print("Index of max AI_CD_diff:", max_index)
print("Maximum AI_CD_diff:", max_ai_cd_diff)
print("Corresponding gauge value:", corresponding_gauge)


___

import pandas as pd
import numpy as np

# Sample dataframe
data = {'pYS': ['1.1', '2.2', 'na', '4.4', 'na']}
df = pd.DataFrame(data)

# Replace 'na' with np.nan
df['pYS'] = df['pYS'].replace('na', np.nan)

# Convert the column to float
df['pYS'] = df['pYS'].astype(float)

print(df)


___

condition = (df['group'] == '1bar') & ((df['po'] + df['p1'] - df['AI_CD']) > 8)

# Drop the rows that meet the condition
df = df.drop(df[condition].index)

___

import pandas as pd

# Assuming df is your DataFrame
# Create a list to hold the indices of rows to drop
rows_to_drop = []

# Iterate through the DataFrame using iterrows
for i, row in df.iterrows():
    if row['group'] == '1bar' and (row['po'] + row['p1'] - row['AI_CD']) > 8:
        rows_to_drop.append(i)

# Drop the rows using the list of indices
df = df.drop(rows_to_drop)

print(df)

___

from PIL import Image

def merge_images(image1_path, image2_path, output_path):
    # Open the images
    image1 = Image.open(image1_path).convert("RGBA")
    image2 = Image.open(image2_path).convert("RGBA")

    # Ensure both images have the same size; if not, resize the second image
    if image1.size != image2.size:
        image2 = image2.resize(image1.size, Image.LANCZOS)

    # Create a new image with the same size as the first image and a transparent background
    merged_image = Image.new("RGBA", image1.size, (0, 0, 0, 0))

    # Paste the first image onto the merged image
    merged_image.paste(image1, (0, 0), image1)

    # Paste the second image onto the merged image
    merged_image.paste(image2, (0, 0), image2)

    # Save the merged image with high quality settings
    merged_image.save(output_path, "PNG")

# Paths to the images to be merged
image1_path = "path/to/first/image.png"
image2_path = "path/to/second/image.png"
output_path = "path/to/output/merged_image.png"

# Merge the images
merge_images(image1_path, image2_path, output_path)

_________________________________

At \textbf{ASML}, I also worked on \textbf{transition cross coefficient (TCC)} optimization. I designed \textbf{rigorous M3D simulations} using \textbf{Tachyon software}, specifically \textbf{FEM+}. I utilized a variety of settings to calculate the optimal TCC number that yields the lowest aerial image critical dimension (AI\_CD) difference between the baseline model and models with fewer TCC numbers. For this purpose, I used different types of settings and masks, such as \textbf{high numerical aperture} with \textbf{low refraction index}, \textbf{high numerical }aperture with binary mask, low numerical aperture with \textbf{low refraction index}, and \textbf{low numerical aperture with binary mask}, each with different mask patterns. These patterns included one-\textbf{dimensional} masks, \textbf{two-dimensional} masks, \textbf{circular} masks, \textbf{elliptical} masks, and \textbf{polygon} masks. I calculated the optimal TCC number, which reduces the run time by 30\% while maintaining accuracy in the aerial image within a specification of 0.1 nm and causing a shift in the x and y directions of less than 0.01 nm. After discussing the results with the research and development team, we \textbf{included this update in the next Tachyon software} release, and the result was also adopted by our customer.


_____

import os

folder_path = 'path/to/your/folder'

if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print(f"Folder '{folder_path}' created.")
else:
    print(f"Folder '{folder_path}' already exists.")


____

TCC(f 
x
​
 ,f 
y
​
 ,f 
x
′
​
 ,f 
y
′
​
 )=∫ 
−∞
∞
​
 S(s 
x
​
 ,s 
y
​
 )⋅P(f 
x
​
 +s 
x
​
 ,f 
y
​
 +s 
y
​
 )⋅P 
∗
 (f 
x
′
​
 +s 
x
​
 ,f 
y
′
​
 +s 
y
​
 )ds 
x
​
 ds 
y
​
 

In this context, 
𝑃
P typically represents the complex transmission function of the mask. This function describes how different spatial frequencies are transmitted through the mask and is critical for understanding and analyzing the mask's imaging performance. 
𝑃
∗
P 
∗
  denotes the complex conjugate of 
𝑃
P.





Is it the projection pupil?
ChatGPT
Yes, 
𝑃
P often represents the projection pupil function in lithography. The projection pupil function describes how light is transmitted through the optical system, including the mask and lens system, and how different spatial frequencies are affected. It plays a crucial role in determining the quality and resolution of the pattern transfer onto the wafer. The complex transmission function 
𝑃
P and its complex conjugate 
𝑃
∗
P 
∗
  are used to evaluate the imaging performance and mask characteristics through the Transmission Cross Coefficient (TCC).




_____

What is the optimal TCC number 
𝑖
i that leads to the maximum absolute difference in AI_CD between the model with 
𝑇
𝐶
𝐶
=
𝑖
TCC=i and the model with 
𝑇
𝐶
𝐶
=
24
TCC=24?


_____

class ExampleClass:
    def method_one(self):
        pass

    def method_two(self):
        pass

    @staticmethod
    def static_method():
        pass

    @classmethod
    def class_method(cls):
        pass

# Function to get all functions of a class by its name
def get_class_methods_by_name(class_name):
    cls = globals().get(class_name)  # Retrieve the class object from globals using its name
    if cls is None:
        raise ValueError(f"Class '{class_name}' not found.")
    
    methods = [func for func in dir(cls) if callable(getattr(cls, func)) and not func.startswith("__")]
    return methods

class_name = "ExampleClass"
methods = get_class_methods_by_name(class_name)
print(methods)


___

import pandas as pd

def read_below_to_dataframe(file_path, search_string="Leaf User CPU time"):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Find the index of the line containing the search string
    start_index = None
    for i, line in enumerate(lines):
        if search_string in line:
            start_index = i + 1  # Start reading from the next line
            break

    if start_index is None:
        raise ValueError(f"'{search_string}' not found in the file.")

    # Read everything below the start_index into a list
    data = []
    for line in lines[start_index:]:
        stripped_line = line.strip()
        if stripped_line:  # Skip empty lines
            data.append(stripped_line.split())  # Assuming the data is space-separated

    # Convert the list of lists to a DataFrame
    df = pd.DataFrame(data)

    return df

# Example usage:
file_path = 'your_file.txt'
df = read_below_to_dataframe(file_path)
print(df)


____

import pandas as pd

def read_below_to_dataframe(file_path, search_string="Leaf User CPU time"):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Find the index of the line containing the search string
    start_index = None
    for i, line in enumerate(lines):
        if search_string in line:
            start_index = i  # Start reading from the line with the search string
            break

    if start_index is None:
        raise ValueError(f"'{search_string}' not found in the file.")

    # Read everything from the start_index into a list
    data = []
    for line in lines[start_index:]:
        stripped_line = line.strip()
        if stripped_line:  # Skip empty lines
            data.append(stripped_line.split())  # Assuming the data is space-separated

    # Convert the list of lists to a DataFrame
    df = pd.DataFrame(data)

    return df

# Example usage:
file_path = 'your_file.txt'
df = read_below_to_dataframe(file_path)
print(df)

____

df.rename(columns={first_column_name

___

import pandas as pd

# Example DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}
df = pd.DataFrame(data)

# Get the name of the first column
first_column_name = df.columns[0]

# Rename the first column
df.rename(columns={first_column_name: 'NewName'}, inplace=True)

print(df)

___import pandas as pd

# Example DataFrame
data = {
    'stage': ['TccPrep-1', 'OtherStage-2', 'Stage(Main_substage)', 'AnotherStage-4'],
    'value': [10, 20, 30, 40]
}
df = pd.DataFrame(data)

# Define the pattern to match either "TccPrep" or "Stage(Main_substage)"
pattern = r'TccPrep|Stage\(Main_substage\)'

# Filter rows where the 'stage' column contains either string
df_filtered = df[df['stage'].str.contains(pattern, regex=True)]

print(df_filtered)

___

import pandas as pd

# Example DataFrame
data = {
    'stage': ['TccPrep_MAINSUBSTAGE', 'OtherStage', 'Stage(Main_MAINSUBSTAGE)', 'AnotherStage'],
    'value': [10, 20, 30, 40]
}
df = pd.DataFrame(data)

# Define the pattern to match either "TccPrep_MAINSUBSTAGE" or "Stage(Main_MAINSUBSTAGE)"
pattern = r'TccPrep_MAINSUBSTAGE|Stage\(Main_MAINSUBSTAGE\)'

# Filter rows where the 'stage' column contains either string
df_filtered = df[df['stage'].str.contains(pattern, regex=True)]

print(df_filtered)

___

import pandas as pd

def read_below_to_dataframe(file_path, search_string="Leaf User CPU time"):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Find the last occurrence of the line containing the search string
    start_index = None
    for i, line in enumerate(lines):
        if search_string in line:
            start_index = i  # Update start_index each time the string is found

    if start_index is None:
        raise ValueError(f"'{search_string}' not found in the file.")

    # Read everything from the start_index into a list
    data = []
    for line in lines[start_index:]:
        stripped_line = line.strip()
        if stripped_line:  # Skip empty lines
            data.append(stripped_line.split())  # Assuming the data is space-separated

    # Convert the list of lists to a DataFrame
    df = pd.DataFrame(data)

    return df

# Example usage:
file_path = 'your_file.txt'
df = read_below_to_dataframe(file_path)
print(df)



___

The relationship between diffraction orders, numerical aperture, and simulation complexity is accurately described.

High NA: Captures more diffraction orders, leading to complex interference patterns and increased simulation complexity.
Low NA: Captures fewer diffraction orders, leading to simpler interference patterns and reduced simulation complexity.
This directly correlates with the earlier point about the impact of TCC reduction on simulation run time being more pronounced in low NA systems.

To summarize:

More diffraction orders = more complex simulations
High NA systems typically involve more diffraction orders
Reducing TCC has a greater impact on simulation time for low NA systems due to their inherent simplicity
This understanding is fundamental to optimizing computational lithography processes.



___

import os
import filecmp

def compare_directories(dir1, dir2):
    # Get the folder names in both directories
    folders1 = sorted([f.name for f in os.scandir(dir1) if f.is_dir()])
    folders2 = sorted([f.name for f in os.scandir(dir2) if f.is_dir()])

    # Check if folder names are the same
    if folders1 != folders2:
        return False, "Folder names do not match."

    # Iterate through each folder and compare files
    for folder in folders1:
        path1 = os.path.join(dir1, folder)
        path2 = os.path.join(dir2, folder)

        files1 = sorted([f.name for f in os.scandir(path1) if f.is_file()])
        files2 = sorted([f.name for f in os.scandir(path2) if f.is_file()])

        # Check if file names in the folders are the same
        if files1 != files2:
            return False, f"Files in folder '{folder}' do not match."

        # Compare the content of each file
        for file in files1:
            file1 = os.path.join(path1, file)
            file2 = os.path.join(path2, file)
            
            if not filecmp.cmp(file1, file2, shallow=False):
                return False, f"File '{file}' in folder '{folder}' differs in content."

    return True, "The directories are identical."

# Example usage:
result, message = compare_directories("/path/to/dir1", "/path/to/dir2")
print(result)  # Will print True if directories are identical, False otherwise
print(message)  # Will print the reason if the directories are not identical


___

import os
import filecmp

def compare_directories(dir1, dir2):
    # Get the folder names in both directories
    folders1 = sorted([f for f in os.listdir(dir1) if os.path.isdir(os.path.join(dir1, f))])
    folders2 = sorted([f for f in os.listdir(dir2) if os.path.isdir(os.path.join(dir2, f))])

    # Check if folder names are the same
    if folders1 != folders2:
        return False, "Folder names do not match."

    # Iterate through each folder and compare files
    for folder in folders1:
        path1 = os.path.join(dir1, folder)
        path2 = os.path.join(dir2, folder)

        files1 = sorted([f for f in os.listdir(path1) if os.path.isfile(os.path.join(path1, f))])
        files2 = sorted([f for f in os.listdir(path2) if os.path.isfile(os.path.join(path2, f))])

        # Check if file names in the folders are the same
        if files1 != files2:
            return False, f"Files in folder '{folder}' do not match."

        # Compare the content of each file
        for file in files1:
            file1 = os.path.join(path1, file)
            file2 = os.path.join(path2, file)
            
            if not filecmp.cmp(file1, file2, shallow=False):
                return False, f"File '{file}' in folder '{folder}' differs in content."

    return True, "The directories are identical."

# Example usage:
result, message = compare_directories("/path/to/dir1", "/path/to/dir2")
print(result)  # Will print True if directories are identical, False otherwise
print(message)  # Will print the reason if the directories are not identical

___

import os
import glob

def list_txt_files(dirs):
    txt_files = []
    for directory in dirs:
        # Search for all .txt files in the directory and its subdirectories
        files = glob.glob(os.path.join(directory, '**', '*.txt'), recursive=True)
        txt_files.extend(files)
    return txt_files

# Example usage
dirs = [
    '/path/to/dir1',
    '/path/to/dir2',
    '/path/to/dir3',
    '/path/to/dir4',
    '/path/to/dir5'
]

txt_files = list_txt_files(dirs)

# Print the list of .txt files with their full paths
for file in txt_files:
    print(file)


___

import os

def get_file_types_in_directories(path):
    file_types_in_dirs = []

    # Traverse through the directories and files in the given path
    for root, dirs, files in os.walk(path):
        file_types = set()
        
        for file in files:
            _, file_extension = os.path.splitext(file)
            if file_extension:
                file_types.add(file_extension)

        if file_types:
            file_types_in_dirs.append(list(file_types))

    return file_types_in_dirs

# Example usage
path = "/your/path/here"
result = get_file_types_in_directories(path)
print(result)


___

find . -type f \( -name "*.txt" -o -name "*.dat" \) | wc -l


___

import os

def find_txt_and_dat_files(directory):
    file_list = []
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt') or file.endswith('.dat'):
                file_list.append(os.path.join(root, file))
    
    return file_list

# Example usage:
directory = '/path/to/your/directory'
files = find_txt_and_dat_files(directory)
print(files)

___

import os

def find_txt_and_dat_files(directory):
    file_list = []
    
    # Get a list of all directories in the tree (including the root directory)
    all_dirs = [os.path.join(dp, f) for dp, dn, filenames in os.walk(directory) for f in dn]
    total_dirs = len(all_dirs)
    
    for i, (root, dirs, files) in enumerate(os.walk(directory), 1):
        print(f'Processing directory {i} out of {total_dirs}: {root}')
        
        for file in files:
            if file.endswith('.txt') or file.endswith('.dat'):
                file_list.append(os.path.join(root, file))
    
    return file_list

# Example usage:
directory = '/path/to/your/directory'
files = find_txt_and_dat_files(directory)
print(f"Found {len(files)} files:")
print(files)


____

import os
import filecmp

def get_file_paths(base_path, subdirs, suffix):
    """
    Generate a list of file paths for each subdirectory and file suffix.
    """
    file_paths = []
    for subdir in subdirs:
        path = os.path.join(base_path, subdir)
        for file in os.listdir(path):
            if file.endswith(suffix):
                file_paths.append(os.path.join(path, file))
    return file_paths

def compare_files(file_list1, file_list2):
    """
    Compare files between two lists.
    """
    if len(file_list1) != len(file_list2):
        raise ValueError("The number of files in both lists must be the same.")

    for file1, file2 in zip(file_list1, file_list2):
        if not filecmp.cmp(file1, file2, shallow=False):
            print(f"Files differ:\n{file1}\n{file2}")

# Define your paths and parameters
base_path1 = "/nfs/PEG/FEM/tpanagio/knife_edge/out_40/"
base_path2 = "/nfs/PEG/FEM/tpanagio/knife_edge/out_39/"
subdirs = ["lib1", "lib2"]  # Add all relevant subdirectories
file_suffix = ".txt"

# Generate file lists
files_out_40 = get_file_paths(base_path1, subdirs, file_suffix)
files_out_39 = get_file_paths(base_path2, subdirs, file_suffix)

# Compare files
compare_files(files_out_40, files_out_39)


___

# Sample dictionary
sample_dict = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3'
}

# Define the file path
file_path = 'output.txt'

# Export the dictionary to a txt file
with open(file_path, 'w') as file:
    for key, value in sample_dict.iteritems():  # Use iteritems() in older Python versions
        file.write('%s: %s\n' % (key, value))   # Use the older string formatting

print("Dictionary has been exported to %s" % file_path)

___

# Sample dictionary
sample_dict = {
    'key1': [0.5, 'pos1'],
    'key2': [0.3, 'pos2'],
    'key3': [0.7, 'pos3']
}

# Define the file path
file_path = 'output.txt'

# Export the dictionary to a txt file (overwrites if exists)
with open(file_path, 'w') as file:
    for key, value in sample_dict.iteritems():  # Use iteritems() in older Python versions
        max_rmse = value[0]
        position = value[1]
        file.write('%s: Max RMSE = %s, Position = %s\n' % (key, max_rmse, position))   # Use the older string formatting

print("Dictionary has been exported to %s" % file_path)

___

# Sample dictionary
sample_dict = {
    'key1': [0.5, 'pos1'],
    'key2': [0.3, 'pos2'],
    'key3': [0.7, 'pos3']
}

# Define the file path
file_path = 'output.txt'

# Export the dictionary to a txt file (overwrites if exists)
with open(file_path, 'w') as file:
    # Write the header
    file.write('Key\tMax RMSE\tPosition\n')
    
    for key, value in sample_dict.iteritems():  # Use iteritems() in older Python versions
        max_rmse = value[0]
        position = value[1]
        # Write each entry in tab-separated format
        file.write('%s\t%s\t%s\n' % (key, max_rmse, position))

print("Dictionary has been exported to %s" % file_path)


___

# Sample dictionary
sample_dict = {
    'key1': [0.5, 'pos1'],
    'key2': [0.3, 'pos2'],
    'key3': [0.7, 'pos3']
}

# Define the file path
file_path = 'output.txt'

# Calculate the maximum length of keys for formatting
max_key_length = max(len(key) for key in sample_dict)

# Open the file for writing (overwrites if exists)
with open(file_path, 'w') as file:
    # Write the header with fixed-width fields
    file.write('%s  %s  %s\n' % ('Key'.ljust(max_key_length), 'Max RMSE'.ljust(9), 'Position'))
    
    for key, value in sample_dict.iteritems():  # Use iteritems() in older Python versions
        max_rmse = value[0]
        position = value[1]
        # Write each entry with fixed-width fields
        file.write('%s  %9.2f  %s\n' % (key.ljust(max_key_length), max_rmse, position))

print "Dictionary has been exported to %s" % file_path

___

# Sample dictionary
sample_dict = {
    'key1': [0.5, 'pos1'],
    'key2': [0.3, 'pos2'],
    'key3': [0.7, 'pos3']
}

# Define the file path
file_path = 'output.txt'

# Calculate the maximum length of keys for formatting
max_key_length = max(len(key) for key in sample_dict)

# Open the file for writing (overwrites if exists)
with open(file_path, 'w') as file:
    # Write the header with fixed-width fields
    file.write('%s  %s  %s\n' % ('Key'.ljust(max_key_length), 'Max RMSE'.ljust(9), 'Position'))
    
    # Write each dictionary entry
    for key, value in sample_dict.iteritems():  # Use iteritems() in older Python versions
        max_rmse = value[0]
        position = value[1]
        # Write each entry with fixed-width fields
        file.write('%s  %9.2f  %s\n' % (key.ljust(max_key_length), max_rmse, position))

print "Dictionary has been exported to %s" % file_path


suppo
___

def find_word_before_real(file_path, specific_word):
    with open(file_path, 'r') as file:
        for line in file:
            words = line.strip().split()
            if specific_word in words and words[-1] == 'real':
                if len(words) > 1:  # Ensure there is a word before 'real'
                    print(words[-2])

# Example usage
file_path = 'your_file.txt'
specific_word = 'target_word'  # Replace with the specific word you're looking for
find_word_before_real(file_path, specific_word)

___

import re

def extract_first_number(path):
    # Find all numbers in the path
    numbers = re.findall(r'\d+', path)
    # Return the first number found as an integer, or a large number if none are found
    return int(numbers[0]) if numbers else float('inf')

def sort_paths_by_first_number(paths):
    return sorted(paths, key=extract_first_number)

# Example usage
paths = [
    "folder12/file34.txt",
    "folder2/file56.txt",
    "folder/file78.txt",
    "folder99/file1.txt"
]

sorted_paths = sort_paths_by_first_number(paths)
print(sorted_paths)

___

import re

def extract_first_number(path):
    # Find all numbers in the path
    numbers = re.findall(r'\d+', path)
    # Return the first number found as an integer, or a large number if none are found
    return int(numbers[0]) if numbers else float('inf')

def sort_paths_by_first_number(paths):
    return sorted(paths, key=lambda path: extract_first_number(path))

# Example usage
paths = [
    "folder12/file34.txt",
    "folder2/file56.txt",
    "folder/file78.txt",
    "folder99/file1.txt"
]

sorted_paths = sort_paths_by_first_number(paths)
for path in sorted_paths:
    print(path)
