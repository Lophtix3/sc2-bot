import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer


class WorkerRushBot(sc2.BotAI):
    async def on_step(self, iteration: int):
        if iteration == 0:
            for worker in self.workers:
                worker.attack(self.enemy_start_locations[0])


if __name__ == "__main__":
    run_game(maps.get("Simple64"), [
        Bot(Race.Zerg, WorkerRushBot()),
        Computer(Race.Protoss, Difficulty.Medium)
    ], realtime=True)
