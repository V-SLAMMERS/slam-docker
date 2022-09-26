import os

DATASET_PATH = "/home/slam/datasets"
KITTI_DATASET_PATH = os.path.join(DATASET_PATH, "kitti", "odometry_gray", "sequences")
EUROC_DATASET_PATH = os.path.join(DATASET_PATH, "euroc")

if os.path.isdir(KITTI_DATASET_PATH):
    kitti_sequences = os.listdir(KITTI_DATASET_PATH)
else:
    print("Kitti dataset not found.")
    kitti_sequences = []

if os.path.isdir(EUROC_DATASET_PATH):
    euroc_sequences = os.listdir(EUROC_DATASET_PATH)
else:
    print("EuRoC dataset not found.")
    euroc_sequences = []

def get_ldso_args():
    while True:
        print("Select a dataset:")
        print("(1) Kitti")
        print("(2) EuRoC")
        print("Enter a number: ", end="")

        choice = input()

        if choice == '1':
            if len(kitti_sequences) == 0:
                print("Kitti dataset not found")
                continue
            print("Select a sequence(Default:00):")
            print(kitti_sequences)
            print("Sequence: ", end="")

            sequence_number = input()

            if sequence_number not in kitti_sequences:
                sequence_number = '00'
            
            exec_path = "/home/slam/LDSO/bin/run_dso_kitti"
            args_preset = "preset=0"
            args_files = f"files={os.path.join(KITTI_DATASET_PATH, sequence_number)}"
            if sequence_number == '03':
                args_calib = f"calib=/home/slam/LDSO/examples/Kitti/Kitti03.txt"
            elif sequence_number == '00' or sequence_number == '01' or sequence_number == '02':
                args_calib = f"calib=/home/slam/LDSO/examples/Kitti/Kitti00-02.txt"
            else:
                # No calibration files are available for sequence 13 to 21.
                args_calib = f"calib=/home/slam/LDSO/examples/Kitti/Kitti04-12.txt"
            
            return f"{exec_path} {args_preset} {args_files} {args_calib}"
        
        elif choice == '2':
            # EuRoC
            if len(euroc_sequences) == 0:
                print("EuRoC dataset not found")
                continue
            print("Select a sequence(Default:MH_01_easy):")
            print(euroc_sequences)
            print("Sequence: ", end="")

            sequence_number = input()

            if sequence_number not in euroc_sequences:
                sequence_number = "MH_01_easy"
            
            exec_path = "/home/slam/LDSO/bin/run_dso_euroc"
            args_preset = "preset=0"
            file_path = os.path.join(EUROC_DATASET_PATH, sequence_number, "mav0", "cam0")
            args_files = f"files={file_path}"
            args_calib = "calib=/home/slam/LDSO/examples/EUROC/EUROC.txt"

            return f"{exec_path} {args_preset} {args_files} {args_calib}"
        
        else:
            print("Invalid choice")
            print()

print("[V-SLAMMERS SLAM Docker Image]")

while True:
    print()
    print("Select the SLAM framework to use")
    print("Enter 'q' to quit")
    print("(1) ORB-SLAM 2")
    print("(2) LDSO")
    print("Enter a number: ", end="")

    choice = input()

    if choice == 'q' or choice == 'Q':
        exit()

    elif choice == '1':
        # Run ORB-SLAM 2
        print("---------------------------")
        print("Running ORB-SLAM 2 with Kitti dataset sequence 0")
        if len(kitti_sequences) == 0:
            print("Kitti dataset not found")
            continue
        os.system("./orb_slam2_w/Examples/Monocular/mono_kitti /home/slam/orb_slam2_w/Vocabulary/ORBvoc.txt /home/slam/orb_slam2_w/Examples/Monocular/KITTI00-02.yaml /home/slam/datasets/kitti/odometry_gray/sequences/00")

    elif choice == '2':
        # Run LDSO
        print("---------------------------")
        print("Running LDSO")
        ldso_arguments = get_ldso_args()
        os.system(ldso_arguments)

    else:
        print("Invalid option")
        print("---------------------------")
        print()

