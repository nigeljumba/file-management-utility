import os
import sys
import shutil
from datetime import datetime

class FileManager:
    def __init__(self):
        self.student_files_dir = "StudentFiles"
        self.archive_dir = os.path.join(self.student_files_dir, "Archive")
        self.log_file = os.path.join(self.student_files_dir, "activity_log.txt")
        
    def log_activity(self, message, is_error=False):
        """TASK 5: Logging System"""
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_message = f"[{timestamp}] {message}"
            
            with open(self.log_file, 'a') as log:
                log.write(log_message + '\n')
                
            if is_error:
                print(f"ERROR: {message}")
            else:
                print(f"LOG: {message}")
                
        except Exception as e:
            print(f"Failed to write to log: {e}")

    def task1_project_initialization(self):
        """TASK 1: Project Initialization"""
        print("\n" + "="*50)
        print("TASK 1: Project Initialization")
        print("="*50)
        
        try:
            # Check if folder exists
            if os.path.exists(self.student_files_dir):
                print(f"✓ Folder '{self.student_files_dir}' already exists")
            else:
                # Create the folder
                os.makedirs(self.student_files_dir)
                print(f"✓ Created folder: '{self.student_files_dir}'")
            
            # Display absolute path
            abs_path = os.path.abspath(self.student_files_dir)
            print(f"✓ Absolute path: {abs_path}")
            
            self.log_activity(f"Project initialized - Folder '{self.student_files_dir}' verified/created")
            return True
            
        except Exception as e:
            error_msg = f"Failed to create folder '{self.student_files_dir}': {e}"
            self.log_activity(error_msg, is_error=True)
            print(f"ERROR: {error_msg}")
            sys.exit(1)

    def task2_file_creation(self):
        """TASK 2: File Creation and Writing"""
        print("\n" + "="*50)
        print("TASK 2: File Creation and Writing")
        print("="*50)
        
        try:
            # Generate file name with current date
            current_date = datetime.now().strftime("%Y-%m-%d")
            file_name = f"records_{current_date}.txt"
            file_path = os.path.join(self.student_files_dir, file_name)
            
            # Prompt user for five student names
            print(f"Enter 5 student names for {file_name}:")
            student_names = []
            for i in range(5):
                name = input(f"Student {i+1}: ").strip()
                if name:
                    student_names.append(name)
                else:
                    student_names.append(f"Student_{i+1}")
            
            # Write names to file
            with open(file_path, 'w') as file:
                for name in student_names:
                    file.write(name + '\n')
            
            # Display success message
            creation_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"✓ Success! File '{file_name}' created at {creation_time}")
            print(f"✓ File saved at: {file_path}")
            
            self.log_activity(f"File '{file_name}' created successfully with 5 student names")
            return file_path
            
        except Exception as e:
            error_msg = f"Failed to create/write file: {e}"
            self.log_activity(error_msg, is_error=True)
            print(f"ERROR: {error_msg}")
            return None

    def task3_file_information(self, file_path):
        """TASK 3: Reading and File Information"""
        print("\n" + "="*50)
        print("TASK 3: Reading and File Information")
        print("="*50)
        
        if not file_path or not os.path.exists(file_path):
            error_msg = "File not found for Task 3"
            self.log_activity(error_msg, is_error=True)
            print(f"ERROR: {error_msg}")
            return
        
        try:
            # Read and display file contents
            print("File contents:")
            print("-" * 20)
            with open(file_path, 'r') as file:
                contents = file.read()
                print(contents)
            print("-" * 20)
            
            # Display file size
            file_size = os.path.getsize(file_path)
            print(f"✓ File size: {file_size} bytes")
            
            # Display last modified date
            mod_time = os.path.getmtime(file_path)
            mod_date = datetime.fromtimestamp(mod_time).strftime("%Y-%m-%d %H:%M:%S")
            print(f"✓ Last modified: {mod_date}")
            
            self.log_activity(f"File information displayed for '{os.path.basename(file_path)}'")
            
        except Exception as e:
            error_msg = f"Failed to read file information: {e}"
            self.log_activity(error_msg, is_error=True)
            print(f"ERROR: {error_msg}")

    def task4_backup_archiving(self, original_file_path):
        """TASK 4: Backup and Archiving"""
        print("\n" + "="*50)
        print("TASK 4: Backup and Archiving")
        print("="*50)
        
        if not original_file_path or not os.path.exists(original_file_path):
            error_msg = "Original file not found for backup"
            self.log_activity(error_msg, is_error=True)
            print(f"ERROR: {error_msg}")
            return
        
        try:
            # Create backup file name
            original_name = os.path.basename(original_file_path)
            backup_name = f"backup_{original_name}"
            backup_path = os.path.join(self.student_files_dir, backup_name)
            
            # Create backup copy
            shutil.copy(original_file_path, backup_path)
            print(f"✓ Backup created: {backup_name}")
            
            # Create Archive folder if it doesn't exist
            if not os.path.exists(self.archive_dir):
                os.makedirs(self.archive_dir)
                print(f"✓ Created archive folder: {self.archive_dir}")
            
            # Move backup to Archive folder
            final_backup_path = os.path.join(self.archive_dir, backup_name)
            shutil.move(backup_path, final_backup_path)
            print(f"✓ Backup moved to archive: {final_backup_path}")
            
            # List all files in Archive folder
            archive_files = os.listdir(self.archive_dir)
            print("✓ Files in Archive folder:")
            for file in archive_files:
                print(f"  - {file}")
            
            self.log_activity(f"Backup '{backup_name}' created and archived successfully")
            
        except Exception as e:
            error_msg = f"Failed to create backup/archive: {e}"
            self.log_activity(error_msg, is_error=True)
            print(f"ERROR: {error_msg}")

    def task5_logging_system(self):
        """TASK 5: Logging System"""
        print("\n" + "="*50)
        print("TASK 5: Logging System")
        print("="*50)
        
        try:
            # This is already implemented throughout the class via log_activity method
            print("✓ Logging system is active")
            print(f"✓ Log file: {self.log_file}")
            
            # Display recent log entries
            if os.path.exists(self.log_file):
                print("\nRecent log entries:")
                print("-" * 40)
                with open(self.log_file, 'r') as log:
                    lines = log.readlines()
                    for line in lines[-5:]:  # Show last 5 entries
                        print(line.strip())
                print("-" * 40)
            
        except Exception as e:
            error_msg = f"Failed to display log information: {e}"
            print(f"ERROR: {error_msg}")

    def task6_advanced_operations(self):
        """TASK 6: Advanced File Operations"""
        print("\n" + "="*50)
        print("TASK 6: Advanced File Operations")
        print("="*50)
        
        try:
            # Ask user if they want to delete a file
            choice = input("Would you like to delete a file from the StudentFiles folder? (Yes/No): ").strip().lower()
            
            if choice == 'yes':
                # Display available files
                files = os.listdir(self.student_files_dir)
                valid_files = [f for f in files if f != "Archive" and os.path.isfile(os.path.join(self.student_files_dir, f))]
                
                if not valid_files:
                    print("No files available for deletion.")
                    return
                
                print("\nAvailable files:")
                for i, file in enumerate(valid_files, 1):
                    print(f"  {i}. {file}")
                
                # Ask for file name to delete
                file_to_delete = input("\nEnter the file name to delete: ").strip()
                file_path = os.path.join(self.student_files_dir, file_to_delete)
                
                if file_to_delete in valid_files and os.path.exists(file_path):
                    os.remove(file_path)
                    print(f"✓ File '{file_to_delete}' deleted successfully")
                    self.log_activity(f"File '{file_to_delete}' deleted by user")
                else:
                    print("✗ File not found or invalid selection")
                    self.log_activity(f"Failed attempt to delete non-existent file '{file_to_delete}'")
            
            # Display remaining files
            remaining_files = os.listdir(self.student_files_dir)
            remaining_files = [f for f in remaining_files if f != "Archive"]
            
            print(f"\n✓ Remaining files in '{self.student_files_dir}':")
            for file in remaining_files:
                file_path = os.path.join(self.student_files_dir, file)
                if os.path.isdir(file_path):
                    print(f"  📁 {file}/")
                else:
                    print(f"  📄 {file}")
                    
        except Exception as e:
            error_msg = f"Failed during advanced operations: {e}"
            self.log_activity(error_msg, is_error=True)
            print(f"ERROR: {error_msg}")

    def run_all_tasks(self):
        """Run all tasks in sequence"""
        print("File Management Utility Starting...")
        print("="*50)
        
        # Task 1
        self.task1_project_initialization()
        
        # Task 2
        file_path = self.task2_file_creation()
        
        # Task 3
        if file_path:
            self.task3_file_information(file_path)
        
        # Task 4
        if file_path:
            self.task4_backup_archiving(file_path)
        
        # Task 5
        self.task5_logging_system()
        
        # Task 6
        self.task6_advanced_operations()
        
        print("\n" + "="*50)
        print("All tasks completed successfully!")
        print("="*50)

def main():
    """Main function to run the file management utility"""
    manager = FileManager()
    manager.run_all_tasks()

if __name__ == "__main__":
    main()