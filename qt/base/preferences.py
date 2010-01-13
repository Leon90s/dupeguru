# Created By: Virgil Dupras
# Created On: 2009-05-03
# Copyright 2010 Hardcoded Software (http://www.hardcoded.net)
# 
# This software is licensed under the "HS" License as described in the "LICENSE" file, 
# which should be included with this package. The terms are also available at 
# http://www.hardcoded.net/licenses/hs_license

from qtlib.preferences import Preferences as PreferencesBase

class Preferences(PreferencesBase):
    # (width, is_visible)
    COLUMNS_DEFAULT_ATTRS = []
    
    def __init__(self):
        PreferencesBase.__init__(self)
        self.reset_columns()
    
    def _load_specific(self, settings, get):
        # load prefs specific to the dg edition
        pass
    
    def _load_values(self, settings, get):
        self.filter_hardness = get('FilterHardness', self.filter_hardness)
        self.mix_file_kind = get('MixFileKind', self.mix_file_kind)
        self.use_regexp = get('UseRegexp', self.use_regexp)
        self.remove_empty_folders = get('RemoveEmptyFolders', self.remove_empty_folders)
        self.destination_type = get('DestinationType', self.destination_type)
        widths = get('ColumnsWidth', self.columns_width)
        # only set nonzero values
        for index, width in enumerate(widths[:len(self.columns_width)]):
            if width > 0:
                self.columns_width[index] = width
        self.columns_visible = get('ColumnsVisible', self.columns_visible)
        self.registration_code = get('RegistrationCode', self.registration_code)
        self.registration_email = get('RegistrationEmail', self.registration_email)
        self._load_specific(settings, get)
    
    def _reset_specific(self):
        # reset prefs specific to the dg edition
        pass
    
    def reset(self):
        self.filter_hardness = 95
        self.mix_file_kind = True
        self.use_regexp = False
        self.remove_empty_folders = False
        self.destination_type = 1
        self.registration_code = ''
        self.registration_email = ''
        self._reset_specific()
    
    def reset_columns(self):
        self.columns_width = [width for width, _ in self.COLUMNS_DEFAULT_ATTRS]
        self.columns_visible = [visible for _, visible in self.COLUMNS_DEFAULT_ATTRS]
    
    def _save_specific(self, settings, set_):
        # save prefs specific to the dg edition
        pass
    
    def _save_values(self, settings, set_):
        set_('FilterHardness', self.filter_hardness)
        set_('MixFileKind', self.mix_file_kind)
        set_('UseRegexp', self.use_regexp)
        set_('RemoveEmptyFolders', self.remove_empty_folders)
        set_('DestinationType', self.destination_type)
        set_('ColumnsWidth', self.columns_width)
        set_('ColumnsVisible', self.columns_visible)
        set_('RegistrationCode', self.registration_code)
        set_('RegistrationEmail', self.registration_email)
        self._save_specific(settings, set_)
    