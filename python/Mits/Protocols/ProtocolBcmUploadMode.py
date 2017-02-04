from Mits.Families.Samsung.BcmUploadModeConsts import COMMANDS, BOOT_COMPLETE, BOOT_TIMEOUT
from Mits.Utils.General import unpack32L
import time


class ProtocolBcmUploadMode:
    # ***************************************************
    def send_tfs_command(self, command):
    def decrypt_passlock(self, passlock):
    def read_passlock(self):
        passlock = self.decrypt_passlock(passlock)
        return passlock
    # Waiting for a phrase coming from the device

    # flag should be True or False
        restart_needed = False
        print "Done!"
        return restart_needed
    def jump_null(self):
    
    def recv_command(self, command):
    def send_upload_command(self, data):
    def before_read(self, start_address, end_address):
        self.send_data(COMMANDS.GET_DATA)
        finished_flag = False
    def after_read_simple(self):
        self.before_read(start, end)
        self.usb_framer.flush()
    def get_dump_start_address(self):
    def get_dump_size(self):
    def restart_device(self):
        return data
    def abort_dump(self):