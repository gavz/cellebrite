from Mits.Utils.upy import upy
from Mits.Utils.ConfigReader import ConfigReader, ScriptConfigObject




class ConfigReaderUFED(ConfigReader) :
    def __init__(self) :
        super(ConfigReaderUFED, self).__init__()




    def _override_phone_params(self) :
        for k, v in self.configuration_dict.iteritems() :
            if type(v) == int :
                value = upy.db_get_int(k, -1)
                if value == -1 :
                    continue
            elif type(v) == bool :
                value = upy.db_get_str(k)
                if value == "" :
                    continue
                value = ScriptConfigObject.eval_bool_value(value)
            elif type(v) == str :
                value = upy.db_get_str(k)
                if value == "" :
                    continue
            print "Overriding %s pre_value(%s) new_value(%s)" % (k, v, value)
            self.configuration_dict[k] = value
            self.config.__setattr__(k, value)


     
    
    def get_config(self, file_name, argument_list) :
        """
        Get the configuration from the UFED 
           - Note that the *file_name* param is irrelevant in this mode 
        """        
        if self.config is None :
            self._set_argument_validation_list(argument_list)
            self.config = ScriptConfigObject()
            for k in argument_list :                
                value_str = str(upy.db_get_str(k))
                self._add_config_value(k, value_str)
            self._validate()
        return self.config
