import os
import shutil

# Define the paths
main_dataset_path = 'Main_Dataset'
extra_dataset_path = 'Main_Dataset_extra'

# Define the list of folder names to keep
keep = ['Boat_Pose_or_Paripurna_Navasana_',
 'Bound_Angle_Pose_or_Baddha_Konasana_',
 'Camel_Pose_or_Ustrasana_',
 'Cat_Cow_Pose_or_Marjaryasana_',
 'Chair_Pose_or_Utkatasana_',
 'Child_Pose_or_Balasana_',
 'Cobra_Pose_or_Bhujangasana_',
 'Cow_Face_Pose_or_Gomukhasana_',
 'Crane_(Crow)_Pose_or_Bakasana_',
 'Downward-Facing_Dog_pose_or_Adho_Mukha_Svanasana_',
 'Eagle_Pose_or_Garudasana_',
 'Extended_Revolved_Side_Angle_Pose_or_Utthita_Parsvakonasana_',
 'Extended_Revolved_Triangle_Pose_or_Utthita_Trikonasana_',
 'Fish_Pose_or_Matsyasana_',
 'Half_Lord_of_the_Fishes_Pose_or_Ardha_Matsyendrasana_',
 'Half_Moon_Pose_or_Ardha_Chandrasana_']

# Create extra directory if it does not exist
if not os.path.exists(extra_dataset_path):
    os.makedirs(extra_dataset_path)

# Iterate over each folder in the Main_Dataset directory
for folder_name in os.listdir(main_dataset_path):
    folder_path = os.path.join(main_dataset_path, folder_name)
    
    # Check if it's a folder and not in the keep list
    if os.path.isdir(folder_path) and folder_name not in keep:
        # Move the folder to Main_Dataset_extra
        shutil.move(folder_path, os.path.join(extra_dataset_path, folder_name))
        print(f"Moved {folder_name} to {extra_dataset_path}")
    else:
        print(f"Kept {folder_name} in {main_dataset_path}")
