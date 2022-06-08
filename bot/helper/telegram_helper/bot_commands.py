from bot import CMD_INDEX


class _BotCommands:
    def __init__(self):
        self.StartCommand = f'start{CMD_INDEX}'
        self.MirrorCommand = f'yuklash{CMD_INDEX}'
        self.UnzipMirrorCommand = f'zipsizyuklash{CMD_INDEX}'
        self.ZipMirrorCommand = f'zipdayuklash{CMD_INDEX}'
        self.CancelMirror = f'bekorqilish{CMD_INDEX}'
        self.CancelAllCommand = f'bekorqilishh{CMD_INDEX}'
        self.ListCommand = f'izlash{CMD_INDEX}'
        self.SearchCommand = f'tizlash{CMD_INDEX}'
        self.StatusCommand = f'status{CMD_INDEX}'
        self.AuthorizedUsersCommand = f'users{CMD_INDEX}'
        self.AuthorizeCommand = f'authorize{CMD_INDEX}'
        self.UnAuthorizeCommand = f'unauthorize{CMD_INDEX}'
        self.AddSudoCommand = f'addsudo{CMD_INDEX}'
        self.RmSudoCommand = f'rmsudo{CMD_INDEX}'
        self.PingCommand = f'ping{CMD_INDEX}'
        self.RestartCommand = f'qaytayuklash{CMD_INDEX}'
        self.StatsCommand = f'statistika{CMD_INDEX}'
        self.HelpCommand = f'yordam{CMD_INDEX}'
        self.LogCommand = f'log{CMD_INDEX}'
        self.CloneCommand = f'klonlash{CMD_INDEX}'
        self.CountCommand = f'hisoblash{CMD_INDEX}'
        self.WatchCommand = f'videoyuklash{CMD_INDEX}'
        self.ZipWatchCommand = f'zipdavideoyuklash{CMD_INDEX}'
        self.QbMirrorCommand = f'tyuklash{CMD_INDEX}'
        self.QbUnzipMirrorCommand = f'tzipsizyuklash{CMD_INDEX}'
        self.QbZipMirrorCommand = f'tzipdayuklash{CMD_INDEX}'
        self.DeleteCommand = f'ochirish{CMD_INDEX}'
        self.ShellCommand = f'shell{CMD_INDEX}'
        self.ExecHelpCommand = f'exechelp{CMD_INDEX}'
        self.LeechSetCommand = f'rasmsozlama{CMD_INDEX}'
        self.SetThumbCommand = f'rasmqoyish{CMD_INDEX}'
        self.LeechCommand = f'tggayuklash{CMD_INDEX}'
        self.UnzipLeechCommand = f'zipsiztggayuklash{CMD_INDEX}'
        self.ZipLeechCommand = f'zipdatggayuklash{CMD_INDEX}'
        self.QbLeechCommand = f'ttggayuklash{CMD_INDEX}'
        self.QbUnzipLeechCommand = f'ttggazipszyuklash{CMD_INDEX}'
        self.QbZipLeechCommand = f'ttggazipdayuklash{CMD_INDEX}'
        self.LeechWatchCommand = f'videotggayuklash{CMD_INDEX}'
        self.LeechZipWatchCommand = f'videotggazipdayuklash{CMD_INDEX}'
        self.RssListCommand = f'rsslist{CMD_INDEX}'
        self.RssGetCommand = f'rssget{CMD_INDEX}'
        self.RssSubCommand = f'rsssub{CMD_INDEX}'
        self.RssUnSubCommand = f'rssunsub{CMD_INDEX}'
        self.RssSettingsCommand = f'rssset{CMD_INDEX}'
        self.EvalCommand = f'eval{CMD_INDEX}'
        self.ExecCommand = f'exec{CMD_INDEX}'
        self.ClearLocalsCommand = f'clearlocals{CMD_INDEX}'

BotCommands = _BotCommands()
