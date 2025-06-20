import os
import time


def get_dirname():
   return os.path.dirname(os.path.abspath(__file__))

__dirname = get_dirname()


def build_rotate_command(pitch, yaw, controller_id):
  return f"set DebugCameraController_{controller_id} ControlRotation (Pitch={pitch},Yaw={yaw},Roll=0)"

def build_toggle_debug_cam_command():
   return "ToggleDebugCamera"

def build_list_cameras_command(controller_type = "DebugCameraController"):
   return f"GetAll {controller_type}"

def mk_dynamic_folder(title = "notitle"):
   date_time = time.strftime("%d-%m-%Y_%H-%M-%S" )
   folder_path = os.path.join(__dirname, "..", "out", f"{title}-{date_time}")
   os.makedirs(folder_path, exist_ok=True)
   return folder_path