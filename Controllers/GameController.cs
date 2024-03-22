using Backend.DALs;
using Backend.DTOs;
using Backend.Services;
using Microsoft.AspNetCore.Mvc;

namespace Backend.Controllers
{
    [ApiController]
    [Route("api")]
    public class GameController : ControllerBase
    {
        private readonly GameService _gameService;
        private readonly UserService _userService;

        public GameController(GameService gameService, UserService userService)
        {
            _gameService = gameService;
            _userService = userService;
        }

        /// <summary>
        /// CRUD operations for games
        /// </summary>

        [HttpPost("games")]
        public async Task<IActionResult> CreateGame([FromBody] Games game)
        {
            try
            {
                if (game == null)
                {
                    // If game is null, return a 400 Bad Request response
                    return BadRequest("Game object is null.");
                }

                await _gameService.AddGame(game);
                return Ok(game);
            }
            catch (Exception e)
            {
                // Log the exception
                Console.WriteLine(e);
                // Return a generic server error response
                return StatusCode(500, "An unexpected error occurred while processing your request.");
            }
        }

        [HttpGet("games")]
        public async Task<IActionResult> GetGames()
        {
            try
            {
                List<Games> games = await _gameService.GetGames();

                if (games == null || games.Count == 0)
                {
                    // If no games found, return a 404 Not Found response
                    return NotFound("No games found.");
                }

                return Ok(games);
            }
            catch (Exception e)
            {
                // Log the exception
                Console.WriteLine(e);
                // Return a generic server error response
                return StatusCode(500, "An unexpected error occurred while processing your request.");
            }
        }

        [HttpGet( "games/{id}")]
        public async Task<IActionResult> GetGame(int id)
        {
            try
            {
                Games game = await _gameService.GetGame(id);

                if (game == null)
                {
                    // If game is null, throw an error with appropriate message
                    return NotFound($"Game with ID {id} not found.");
                }

                return Ok(game);
            }
            catch (Exception e)
            {
                // Log the exception
                Console.WriteLine(e);
                // Return a generic server error response
                return StatusCode(500, "An unexpected error occurred while processing your request.");
            }
        }

        [HttpDelete("games/{id}")]
        public async Task<IActionResult> DeleteGame(int id)
        {
            try
            {
                Games game = await _gameService.GetGame(id);

                if (game == null)
                {
                    // If game is null, throw an error with appropriate message
                    return NotFound($"Game with ID {id} not found.");
                }

                await _gameService.DeleteGame(game);
                return Ok();
            }
            catch (Exception e)
            {
                // Log the exception
                Console.WriteLine(e);
                // Return a generic server error response
                return StatusCode(500, "An unexpected error occurred while processing your request.");
            }
        }

        /// <summary>
        /// CRUD operations for users
        /// </summary>

        [HttpPost("users")]
        public async Task<IActionResult> CreateUser([FromBody] Users user)
        {
            try
            {
                if (user == null)
                {
                    // If user is null, return a 400 Bad Request response
                    return BadRequest("User object is null.");
                }

                await _userService.AddUser(user);
                return Ok(user);
            }
            catch (Exception e)
            {
                // Log the exception
                Console.WriteLine(e);
                // Return a generic server error response
                return StatusCode(500, "An unexpected error occurred while processing your request.");
            }
        }

        [HttpGet("users")]
        public async Task<IActionResult> GetUsers()
        {
            try
            {
                List<Users> users = await _userService.GetUsers();

                if (users == null || users.Count == 0)
                {
                    // If no users found, return a 404 Not Found response
                    return NotFound("No users found.");
                }

                return Ok(users);
            }
            catch (Exception e)
            {
                // Log the exception
                Console.WriteLine(e);
                // Return a generic server error response
                return StatusCode(500, "An unexpected error occurred while processing your request.");
            }
        }

        [HttpGet("users/{id}")]
        public async Task<IActionResult> GetUser(int id)
        {
            try
            {
                Users user = await _userService.GetUser(id);

                if (user == null)
                {
                    // If user is null, throw an error with appropriate message
                    return NotFound($"User with ID {id} not found.");
                }

                return Ok(user);
            }
            catch (Exception e)
            {
                // Log the exception
                Console.WriteLine(e);
                // Return a generic server error response
                return StatusCode(500, "An unexpected error occurred while processing your request.");
            }
        }

        [HttpDelete("users/{id}")]
        public async Task<IActionResult> DeleteUser(int id)
        {
            try
            {
                Users user = await _userService.GetUser(id);

                if (user == null)
                {
                    // If user is null, throw an error with appropriate message
                    return NotFound($"User with ID {id} not found.");
                }

                await _userService.DeleteUser(user);
                return Ok();
            }
            catch (Exception e)
            {
                // Log the exception
                Console.WriteLine(e);
                // Return a generic server error response
                return StatusCode(500, "An unexpected error occurred while processing your request.");
            }
        }

        /// <summary>
        /// CRUD operations for images
        /// </summary>

        [HttpPost("images")]
        public async Task<IActionResult> CreateImage([FromBody] Images image)
        {
            try
            {
                if (image == null)
                {
                    // If image is null, return a 400 Bad Request response
                    return BadRequest("Image object is null.");
                }

                await _gameService.AddImage(image);
                return Ok(image);
            }
            catch (Exception e)
            {
                // Log the exception
                Console.WriteLine(e);
                // Return a generic server error response
                return StatusCode(500, "An unexpected error occurred while processing your request.");
            }
        }

        [HttpGet("images/{id}")]
        public async Task<IActionResult> GetImage(int id)
        {
            try
            {
                Images image = await _gameService.GetImage(id);

                if (image == null)
                {
                    // If image is null, throw an error with appropriate message
                    return NotFound($"Image with ID {id} not found.");
                }

                return Ok(image);
            }
            catch (Exception e)
            {
                // Log the exception
                Console.WriteLine(e);
                // Return a generic server error response
                return StatusCode(500, "An unexpected error occurred while processing your request.");
            }
        }

        [HttpDelete("images/{id}")]
        public async Task<IActionResult> DeleteImage(int id)
        {
            try
            {
                Images image = await _gameService.GetImage(id);

                if (image == null)
                {
                    // If image is null, throw an error with appropriate message
                    return NotFound($"Image with ID {id} not found.");
                }

                await _gameService.DeleteImage(image);
                return Ok();
            }
            catch (Exception e)
            {
                // Log the exception
                Console.WriteLine(e);
                // Return a generic server error response
                return StatusCode(500, "An unexpected error occurred while processing your request.");
            }
        }

        /// <summary>
        /// Check if there is a user with the given username and password
        /// </summary>

        [HttpPost("login")]
        public async Task<IActionResult> CheckUser([FromBody] UserDTO checkUser)
        {
            try
            {
                List<Users> users = await _userService.GetUsers();

                if (users == null || users.Count == 0)
                {
                    // If no users found, return a 404 Not Found response
                    return NotFound("No users found.");
                }

                Users user = users.FirstOrDefault(u => u.Email == checkUser.Email && u.Password == checkUser.Password);

                if (user == null)
                {
                    // If user is null, throw an error with appropriate message
                    return NotFound("Could not log in!");
                }

                return Ok();
            }
            catch (Exception e)
            {
                // Log the exception
                Console.WriteLine(e);
                // Return a generic server error response
                return StatusCode(500, "An unexpected error occurred while processing your request.");
            }
        }
    }
}
