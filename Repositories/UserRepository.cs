using Backend.DALs;
using Backend.DataAccess;
using Microsoft.EntityFrameworkCore;

namespace Backend.Repositories
{
    public class UserRepository
    {
        private readonly DBContext _context;

        public UserRepository(DBContext context)
        {
            _context = context;
        }

        public async Task<Users> AddUser(Users user)
        {
            _context.Users.Add(user);
            await _context.SaveChangesAsync();
            return user;
        }

        public async Task<List<Users>> GetUsers()
        {
            return await _context.Users.ToListAsync();
        }

        public async Task<Users> GetUser(int id)
        {
            return await _context.Users.FindAsync(id);
        }

        public async Task DeleteUser(Users user)
        {
            _context.Users.Remove(user);
        }
    }
}
