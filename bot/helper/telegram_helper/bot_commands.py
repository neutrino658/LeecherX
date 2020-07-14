class _BotCommands:
    def __init__(self):
        self.StartCommand = 'wakeup'
        self.MirrorCommand = 'mirror'
        self.TarMirrorCommand = 'tarmirror'
        self.CancelMirror = 'cancel'
        self.CancelAllCommand = 'cancelall'
        self.ListCommand = 'list'
        self.StatusCommand = 'status'
        self.AuthorizeCommand = 'auth'
        self.UnAuthorizeCommand = 'unauth'
        self.PingCommand = 'pong'
        self.RestartCommand = 'reboot'
        self.StatsCommand = 'stats'
        self.HelpCommand = 'help'
        self.LogCommand = 'log'
        self.CloneCommand = "rclone"
        self.WatchCommand = 'ytdl'
        self.TarWatchCommand = 'tarytdl'

BotCommands = _BotCommands()
