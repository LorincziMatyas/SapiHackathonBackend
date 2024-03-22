using Backend.DALs;
using Backend.Repositories;

namespace Backend.Services
{
    public class UserService
    {
        private readonly UserRepository _userRepository;

        public UserService(UserRepository userRepository)
        {
            _userRepository = userRepository;
        }

        public async Task<Users> AddUser(Users user)
        {
            return await _userRepository.AddUser(user);
        }

        public async Task<List<Users>> GetUsers()
        {
            return await _userRepository.GetUsers();
        }

        public async Task<Users> GetUser(int id)
        {
            return await _userRepository.GetUser(id);
        }

        public async Task DeleteUser(Users user)
        {
            await _userRepository.DeleteUser(user);
        }
    }
}
