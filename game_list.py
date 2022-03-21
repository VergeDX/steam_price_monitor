from game_model import SteamGame

OneShot: SteamGame = SteamGame("OneShot", 420530, 1800)
Florence: SteamGame = SteamGame("Florence", 1102130, 1000)

monitoring_games: list[SteamGame] = [OneShot, Florence]
