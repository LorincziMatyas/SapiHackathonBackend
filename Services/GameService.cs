using Backend.DALs;
using Backend.Repositories;

namespace Backend.Services
{
    public class GameService
    {
        private readonly GameRepository _gameRepository;

        public GameService(GameRepository gameRepository)
        {
            _gameRepository = gameRepository;
        }

        public async Task<Games> AddGame(Games game)
        {
            return await _gameRepository.AddGame(game);
        }

        public async Task<List<Games>> GetGames()
        {
            return await _gameRepository.GetGames();
        }

        public async Task<Games> GetGame(int id)
        {
            return await _gameRepository.GetGame(id);
        }

        public async Task AddImage(Images image)
        {
            await _gameRepository.AddImage(image);
        }

        public async Task<Images> GetImage(int id)
        {
            return await _gameRepository.GetImage(id);
        }

        public async Task DeleteGame(Games game)
        {
            await _gameRepository.DeleteGame(game);
        }

        public async Task DeleteImage(Images image)
        {
            await _gameRepository.DeleteImage(image);
        }
    }
}
