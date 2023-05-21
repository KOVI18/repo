import os, xbmc, xbmcaddon

#########################################################
### User Edit Variables #################################
#########################################################
ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = '[COLOR red]KODI-VAVOO-TV-Stube [/COLOR][COLOR skyblue]Wizard[/COLOR]'
EXCLUDES       = [ADDON_ID]
# Enable/Disable the text file caching with 'Yes' or 'No' and age being how often it rechecks in minutes
CACHETEXT      = 'Yes'
CACHEAGE       = 30
# Text File with build info in it.
BUILDFILE      = 'https://kovi.ml/addon/wizard/data/install.txt'
# How often you would list it to check for build updates in days
# 0 being every startup of kodi
UPDATECHECK    = 0
# Text File with apk info in it.
APKFILE        = 'https://kovi.ml/addon/wizard/data/apk.txt'
# Text File with retro info in it.  Leave as 'http://' to ignore
RETROFILE      = ''
# Text File with Youtube Videos urls.  Leave as 'http://' to ignore
YOUTUBETITLE   = 'Tutorials auf Youtube'
YOUTUBEFILE    = 'https://kovi.ml/addon/wizard/data/youtube.txt'
# Text File for addon installer.  Leave as 'http://' to ignore
ADDONFILE      = 'https://kovi.ml/addon/wizard/data/addons.txt'
# Text File for advanced settings.  Leave as 'http://' to ignore
ADVANCEDFILE   = 'https://kovi.ml/addon/wizard/data/advancedsettings.txt'
# Text file for roms and emus
ROMPACK        = ''
EMUAPKS        = ''

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
ICONBUILDS     = 'https://kovi.ml/addon/wizard/img/builds.png'
ICONMAINT      = 'https://kovi.ml/addon/wizard/img/instandhaltung.png'
ICONAPK        = 'https://kovi.ml/addon/wizard/img/apkinstaller.png'
ICONRETRO      = 'https://kovi.ml/addon/wizard/img/retro.png'
ICONADDONS     = 'https://kovi.ml/addon/wizard/img/addoninstaller.png'
ICONYOUTUBE    = 'https://kovi.ml/addon/wizard/img/youtube.png'
ICONSAVE       = 'https://kovi.ml/addon/wizard/img/savedata.png'
ICONTRAKT      = 'https://kovi.ml/addon/wizard/img/keeptrakt.png'
ICONREAL       = 'https://kovi.ml/addon/wizard/img/keepdebrid.png'
ICONLOGIN      = 'https://kovi.ml/addon/wizard/img/log.png'
ICONCONTACT    = 'https://kovi.ml/addon/wizard/img/telegram.png'
ICONSETTINGS   = 'https://kovi.ml/addon/wizard/img/settings.png'
# Hide the ====== seperators 'Yes' or 'No'
HIDESPACERS    = 'Yes'
# Character used in seperator
SPACER         = ''

# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1         = 'deepskyblue'
COLOR2         = 'white'
# Primary menu items   / %s is the menu item and is required
THEME1         = '[COLOR '+COLOR1+'][B][I]([COLOR '+COLOR2+'])[/B][/COLOR] [COLOR '+COLOR2+']%s[/COLOR][/I]'
# Build Names          / %s is the menu item and is required
THEME2         = '[COLOR '+COLOR2+']%s[/COLOR]'
# Alternate items      / %s is the menu item and is required
THEME3         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Current Build Header / %s is the menu item and is required
THEME4         = '[COLOR '+COLOR1+']Aktuelles Build:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
# Current Theme Header / %s is the menu item and is required
THEME5         = '[COLOR '+COLOR1+']Aktuelles Theme:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT    = 'No'
# You can add \n to do line breaks
CONTACT        = 'Bitte folgen Sie den Anweisungen zur Installation. \nBei Fragen oder Anregungen erreichen Sie uns per Telegram Kanal bzw. Gruppe.'
#Images used for the contact window.  http:// for default icon and fanart
CONTACTICON    = 'https://kovi.ml/addon/wizard/img/telegram.png'
CONTACTFANART  = 'https://kovi.ml/addon/wizard/img/fanart.png'
#########################################################

#########################################################
### AUTO UPDATE #########################################
########## FOR THOSE WITH NO REPO #######################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE     = 'yes'
# Url to wizard version
WIZARDFILE     = ''
#########################################################

#########################################################
### AUTO INSTALL ########################################
########## REPO IF NOT INSTALLED ########################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL    = 'Yes'
# Addon ID for the repository
REPOID         = 'repository.kovi18'
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML   = 'https://kovi.ml/repo/addons.xml'
# Url to folder zip is located in
REPOZIPURL     = 'https://kovi.ml/repo/repository.kovi18/'
#########################################################

#########################################################
### NOTIFICATION WINDOW##################################
#########################################################
# Enable Notification screen Yes or No
ENABLE         = 'Yes'
# Url to notification file
NOTIFICATION   = 'https://kovi.ml/addon/wizard/data/notification.txt'
# Use either 'Text' or 'Image'
HEADERTYPE     = 'Text'
# Font size of header
FONTHEADER     = 'Font15'
HEADERMESSAGE  = 'Mediencenter Installation'
# url to image if using Image 424x180
HEADERIMAGE    = 'https://kovi.ml/addon/wizard/img/kovibanner.png'
# Font for Notification Window
FONTSETTINGS   = 'Font14'
# Background for Notification Window
BACKGROUND     = 'https://kovi.ml/addon/wizard/img/infobackground.jpg'
#########################################################


ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = '[B][COLORdeepskyblue]KOVI[/B][/COLOR] [COLORwhite]Wizard[/COLOR]'
EXCLUDES       = [ADDON_ID]
# Text File with build info in it.
BUILDFILE      = 'https://kovi.ml/addon/wizard/data/install.txt'
# How often you would list it to check for build updates in days
# 0 being every startup of kodi
UPDATECHECK    = 0
# Text File with apk info in it.
APKFILE        = 'https://kovi.ml/addon/wizard/data/apk.txt'
# Text File with Youtube Videos urls.  Leave as 'http://' to ignore
YOUTUBETITLE   = 'Tutorials auf Youtube'
YOUTUBEFILE    = 'https://kovi.ml/addon/wizard/data/youtube.txt'
# Text File for addon installer.  Leave as 'http://' to ignore
ADDONFILE      = 'https://kovi.ml/addon/wizard/data/addons.txt'
# Text File for advanced settings.  Leave as 'http://' to ignore
ADVANCEDFILE   = 'https://kovi.ml/addon/wizard/data/advancedsettings.txt'

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
ICONBUILDS     = 'https://kovi.ml/addon/wizard/img/builds.png'
ICONMAINT      = 'https://kovi.ml/addon/wizard/img/instandhaltung.png'
ICONAPK        = 'https://kovi.ml/addon/wizard/img/apkinstaller.png'
ICONADDONS     = 'https://kovi.ml/addon/wizard/img/addoninstaller.png'
ICONADVANCED   = 'https://kovi.ml/addon/wizard/img/advanced.png'
ICONBACKUP     = 'https://kovi.ml/addon/wizard/img/backup.png'
ICONSPEED      = 'https://kovi.ml/addon/wizard/img/networktools.png'
ICONYOUTUBE    = 'https://kovi.ml/addon/wizard/img/youtube.png'
ICONSAVE       = 'https://kovi.ml/addon/wizard/img/savedata.png'
ICONTRAKT      = 'https://kovi.ml/addon/wizard/img/keeptrakt.png'
ICONREAL       = 'https://kovi.ml/addon/wizard/img/keepdebrid.png'
ICONCONTACT    = 'https://kovi.ml/addon/wizard/img/telegram.png'
ICONSETTINGS   = 'https://kovi.ml/addon/wizard/img/settings.png'
ICONCLEAN      = 'https://kovi.ml/addon/wizard/img/reinigung.png'
ICONLOG        = 'https://kovi.ml/addon/wizard/img/log.png'
ICONPAY        = 'https://kovi.ml/addon/wizard/img/paypal.png'
# Hide the ====== seperators 'Yes' or 'No'
HIDESPACERS    = 'YES'
# Character used in seperator
SPACER         = ''

# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1         = 'deepskyblue'
COLOR2         = 'white'
# Primary menu items   / %s is the menu item and is required
THEME1         = '[COLOR '+COLOR1+'][B][I][COLOR '+COLOR2+'][/COLOR][/B][/COLOR] [COLOR '+COLOR2+']%s[/COLOR][/I]'
# Build Names          / %s is the menu item and is required
THEME2         = '[COLOR '+COLOR2+']%s[/COLOR]'
# Alternate items      / %s is the menu item and is required
THEME3         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Current Build Header / %s is the menu item and is required
THEME4         = '[COLOR '+COLOR1+']Aktuelles Build:[/COLOR] [B][COLOR '+COLOR2+']%s[/COLOR][/B]'
# Current Theme Header / %s is the menu item and is required
THEME5         = '[COLOR '+COLOR1+']Aktuelles Theme:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT    = 'No'
# You can add \n to do line breaks
CONTACT        = 'Bitte folgen Sie den Anweisungen zur Installation. \nBei Fragen oder Anregungen erreichen Sie uns per Telegram Kanal bzw. Gruppe.'
#Images used for the contact window.  http:// for default icon and fanart
CONTACTICON    = 'https://kovi.ml/addon/wizard/img/telegram.png'
CONTACTFANART  = 'https://kovi.ml/addon/wizard/img/fanart.png'
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
ENABLE         = 'Yes'
# Url to notification file
NOTIFICATION   = 'https://kovi.ml/addon/wizard/data/notification.txt'
# Use either 'Text' or 'Image'
HEADERTYPE     = 'Image'
HEADERMESSAGE  = 'Mediencenter KOVI'
# url to image if using Image 424x180
HEADERIMAGE    = 'https://kovi.ml/addon/wizard/img/kovibanner.png'
# Background for Notification Window
BACKGROUND     = 'https://kovi.ml/addon/wizard/img/infobackground.jpg'
		
################################################################################
#                 modified by KOVI - / 10.2022            #
################################################################################
