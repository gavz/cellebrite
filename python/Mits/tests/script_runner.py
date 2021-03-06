"""
This is the script runner for Python-UFED solution 
it should help the debugging :
    * MAIN_EXEC_SCRIPT - contains the script file name -
                         received from the UFED in the global scope
    * STDOUT_FILE_NAME   - filename for the stdout (None - stdout unchanged) 
    * EXCEPTIONS_TB_NAME - filename for the exceptions 
                         (None - exceptions will be written to stdout )                         
    * MAIN_EXEC_SCRIPT - contains the script file name -
                         received from the UFED in the global scope
    * THROW_EXCEPTIONS - True - the exception will be re-thrown
                         False - the exception will be caught and 
                                script should exit normally with 0
"""


###########
#
# The following section solves runtime error R6034
#
###########
import os


def try_list_dir(path):
    try :
        return os.listdir(path)
    except Exception, e :
        return ''




os.environ['path'] = ";".join(
    [path for path in os.environ['path'].split(";") 
     if "msvcr90.dll" not in map((lambda x:x.lower()), try_list_dir(path))])


######################




import sys, traceback




STDOUT_FILE_NAME = None
#STDOUT_FILE_NAME = r'c:\temp\stdout_pythonUFED.log'


EXCEPTIONS_TB_NAME = None
#EXCEPTIONS_TB_NAME = r'c:\temp\exception_pythonUFED.log'


THROW_EXCEPTIONS = True
 
try :
    stdout_file = None
    sys_stdout_prev = None
    if STDOUT_FILE_NAME is not None :
        sys_stdout_prev = sys.stdout 
        stdout_file = file(STDOUT_FILE_NAME, 'w', buffering = 0)
        sys.stdout = stdout_file 
    
    print "*** STDOUT ***"
    print "Running %s" % MAIN_EXEC_SCRIPT 
    execfile(MAIN_EXEC_SCRIPT)
    
    
except Exception, e:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    file_ = sys.stdout
    if EXCEPTIONS_TB_NAME is not None :        
        file_ = file(EXCEPTIONS_TB_NAME, 'w', buffering = 0)
        
    file_.write("Exception :\n")
    traceback.print_exception(exc_type, exc_value, exc_traceback, file=file_)
    
    file_.write("Traceback :\n")
    traceback.print_tb(exc_traceback, file=file_)
    
    if EXCEPTIONS_TB_NAME is not None: 
        file_.close()
        
    if stdout_file is not None :
        sys.stdout = sys_stdout_prev
        stdout_file.close()
        
        
    if THROW_EXCEPTIONS :
        raise
    # end nicely - with success   


