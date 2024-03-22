using Backend.DALs;
using Backend.DataAccess;
using Microsoft.EntityFrameworkCore;

namespace Backend.Repositories
{
    public class GameRepository
    {
        private readonly DBContext _context;

        public GameRepository(DBContext context)
        {
            _context = context;
        }

        public async Task<Games> AddGame(Games game)
        {
            _context.Games.Add(game);
            _context.SaveChanges();
            return game;
        }

        public async Task<List<Games>> GetGames()
        {
            return await _context.Games.ToListAsync();
        }

        public async Task<Games> GetGame(int id)
        {

            return _context.Games.FirstOrDefault(g => g.Id == id);
        }

        public async Task AddImage(Images image)
        {
            _context.Images.Add(image);
        }

        public async Task<Images> GetImage(int id)
        {
            return _context.Images.FirstOrDefault(i => i.Id == id);
        }

        public async Task DeleteGame(Games game)
        {
            _context.Games.Remove(game);
        }

        public async Task DeleteImage(Images image)
        {
            _context.Images.Remove(image);
        }
    }
}
