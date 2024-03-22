using Backend.DALs;
using Backend.Services;
using Microsoft.AspNetCore.Mvc;

namespace Backend.Controllers
{
    [ApiController]
    [Route("api/games")]
    public class GameController : ControllerBase
    {
        private readonly GameService _gameService;

        public GameController(GameService gameService)
        {
            _gameService = gameService;
        }

        [HttpPost(Name = "")]
        public async Task<IActionResult> CreateGame([FromBody] Games game)
        {
            _gameService.AddGame(game);
            return Ok(game);
        }


        [HttpGet(Name = "")]
        public async Task<List<Games>> GetGames()
        {
            return await _gameService.GetGames(); ;
        }

        [HttpGet("{id}", Name = "{id}")]
        public async Task<Games> GetGame(int id)
        {
            return await _gameService.GetGame(id);
        }




        public static List<Games> GenerateMockData(int count)
        {
            List<Games> mockData = new List<Games>();

            Random rand = new Random();

            for (int i = 0; i < count; i++)
            {
                Games game = new Games
                {
                    Id = i + 1,
                    Name = GenerateRandomName(rand),
                    Description = GenerateRandomDescription(rand),
                    LearningPercentage = rand.Next(0, 101) // Random percentage between 0 and 100
                };

                mockData.Add(game);
            }

            return mockData;
        }

        private static string GenerateRandomName(Random rand)
        {
            // Define the character set from which the name will be generated
            string charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

            // Generate a random length for the name (between 5 and 10 characters)
            int length = rand.Next(5, 11);

            // Generate the name by randomly selecting characters from the charset
            string name = "";
            for (int i = 0; i < length; i++)
            {
                name += charset[rand.Next(0, charset.Length)];
            }

            return name;
        }

        private static string GenerateRandomDescription(Random rand)
        {
            // Define some sample words for description generation
            string[] words = { "exciting", "adventurous", "challenging", "fun", "engaging", "educational", "entertaining" };

            // Generate a random length for the description (between 10 and 20 words)
            int length = rand.Next(10, 21);

            // Generate the description by randomly selecting words from the array
            string description = "";
            for (int i = 0; i < length; i++)
            {
                description += words[rand.Next(0, words.Length)] + " ";
            }

            return description.Trim(); // Trim any trailing space
        }

    }
}
