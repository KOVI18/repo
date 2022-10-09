import os, xbmc, xbmcaddon

#########################################################
### User Edit Variables #################################
#########################################################
ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = 'KOVI Setup'
EXCLUDES       = [ADDON_ID]
# Text File with build info in it.
BUILDFILE      = 'http://'
#/files/wizard/Build.txt How often you would list it to check for build updates in days
# 0 being every startup of
UPDATECHECK    = 0
# Text File with apk info in it.
APKFILE        = 'http://openkd.tv/homepage/files/wizard/ApK/txt/android.txt'
# Text File with Youtube Videos urls.  Leave as 'http://' to ignore
YOUTUBETITLE   = 'Youtube Anleitungen'
YOUTUBEFILE    = 'http://openkd.tv/homepage/files/wizard/youtube.txt'
# Text File for addon installer.  Leave as 'http://' to ignore
ADDONFILE      = 'http://openkd.tv/homepage/files/wizard/addons.txt'
# Text File for advanced settings.  Leave as 'http://' to ignore
ADVANCEDFILE   = 'http://openkd.tv/homepage/files/wizard/advancedsettings.txt'

# Dont need to edit just here for icons stored locally
PATH           = xbmcaddon.Addon().getAddonInfo('path')
ART            = os.path.join(PATH, 'resources', 'art')

#########################################################
### THEMING MENU ITEMS ##################################
#########################################################
# If you want to use locally stored icons the place them in the Resources/Art/
# folder of the wizard then use os.path.join(ART, 'imagename.png')
# do not place quotes around os.path.join
# Example:  ICONMAINT     = os.path.join(ART, 'mainticon.png')
#           ICONSETTINGS  = 'http://aftermathwizard.net/repo/wizard/settings.png'
# Leave as http:// for default icon
ICONBUILDS     = 'http://kovi.ga/setup/setup001.png'
ICONMAINT      = 'http://kovi.ga/setup/setup002.png'
ICONAPK        = 'http://kovi.ga/setup/setup003.png'
ICONADDONS     = 'http://kovi.ga/setup/setup004.png'
ICONMAINT      = 'http://kovi.ga/setup/setup005.png'
ICONAPK        = 'http://kovi.ga/setup/setup006.png'
ICONSPEED      = 'http://kovi.ga/setup/setup007.png'
ICONMAINT      = 'http://kovi.ga/setup/setup008.png'
ICONAPK        = 'http://kovi.ga/setup/setup009.png'
ICONTRAKT      = 'http://kovi.ga/setup/setup010.png'
ICONMAINT      = 'http://kovi.ga/setup/setup011.png'
ICONAPK        = 'http://kovi.ga/setup/setup012.png'
ICONSETTINGS   = 'http://kovi.ga/setup/setup013.png'
ICONMAINT      = 'http://kovi.ga/setup/setup014.png'
ICONAPK        = 'http://kovi.ga/setup/setup015.png'
ICONPAY        = 'http://kovi.ga/setup/setup016.png'
# Hide the ====== seperators 'Yes' or 'No'
HIDESPACERS    = 'YES'
# Character used in seperator
SPACER         = ''

# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1         = 'cyan'
COLOR2         = 'azure'
# Primary menu items   / %s is the menu item and is required
THEME1         = '[COLOR '+COLOR1+'][B][I][COLOR '+COLOR2+'][/COLOR][/B][/COLOR] [COLOR '+COLOR2+']%s[/COLOR][/I]'
# Build Names          / %s is the menu item and is required
THEME2         = '[COLOR '+COLOR2+']%s[/COLOR]'
# Alternate items      / %s is the menu item and is required
THEME3         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Current Build Header / %s is the menu item and is required
THEME4         = '[COLOR '+COLOR1+']Installiertes Build:[/COLOR] [B][COLOR '+COLOR2+']%s[/COLOR][/B]'
# Current Theme Header / %s is the menu item and is required
THEME5         = '[COLOR '+COLOR1+']Aktuelles Theme:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT    = 'No'
# You can add \n to do line breaks
CONTACT        = ''
#Images used for the contact window.  http:// for default icon and fanart
CONTACTICON    = 'http://kovi.ga/setup/setup001.png'
CONTACTFANART  = 'http://kovi.ga/setup/setup001.png'
#########################################################

#########################################################
### AUTO UPDATE #########################################
########## FOR THOSE WITH NO REPO #######################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE     = 'No'
# Url to wizard version
WIZARDFILE     = ''
#########################################################

#########################################################
### AUTO INSTALL ########################################
########## REPO IF NOT INSTALLED ########################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL    = 'No'
# Addon ID for the repository
REPOID         = ''
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML   = ''
# Url to folder zip is located in
REPOZIPURL     = ''
#########################################################

#########################################################
### NOTIFICATION WINDOW##################################
#########################################################
# Enable Notification screen Yes or No
ENABLE         = 'No'
# Url to notification file
NOTIFICATION   = ''
# Use either 'Text' or 'Image'
HEADERTYPE     = ''
HEADERMESSAGE  = ''
# url to image if using Image 424x180
HEADERIMAGE    = 'http://kovi.ga/setup/setup001.png'
# Background for Notification Window
BACKGROUND     = 'http://kovi.ga/setup/setup001.png'
		
################################################################################
#                 modified by OpenKD Support - Group / 10.2019                 #
################################################################################