from Mits.Families.Samsung.BcmUploadMode        import FamilyBcmSerial, FamilyBcmUploadMode
PASSWORD_EXCEPTION = "Password is!@#$%^"
class ClientBcmUploadMode(object):
    def __init__(self):
    def connect(self):
    # Password's length must be between 4 to 8.
    @staticmethod 
        data_hash = data.decode("base64")
        i = start
        raise Exception("Couldn't find the password...")
        # Examples:



    
    def into_upload_mode(self, phone_already_booted = False):
        upy.ui_async_operation("Please wait", "Initializing...")
        print "Please press the middle button on the device (Enter) and wait until UPLOAD mode is initiated"
        self.usb_family.close()
    def restore_debug_level_and_finalize(self):        
        upy.ui_msg_continue("To finalize the dump safely, please follow the following instructions: \n1. Disconnect the phone\n2. Remove the BATTERY\n3. Insert the BATTERY\n4. Connect cable A with black tip T-130 to the computer (the phone SHOULD NOT be connected yet)\n5. Press continue", "Finalize Extraction")
        self.serial_family.protocols['BcmUploadMode'].close_serial()
        #upy.target_finalize_write()
    def close(self):