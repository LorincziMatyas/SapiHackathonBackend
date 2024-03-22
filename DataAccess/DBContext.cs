using Backend.DALs;
using Microsoft.EntityFrameworkCore;

namespace Backend.DataAccess
{
    public class DBContext : DbContext
    {
        public DBContext(DbContextOptions<DBContext> options) : base(options) { }

        public DbSet<Users> Users { get; set; }
        public DbSet<Games> Games { get; set; }
        public DbSet<Steps> Steps { get; set; }
        public DbSet<Images> Images { get; set; }

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            base.OnConfiguring(optionsBuilder);
            const string connectionString = "Host=localhost;Port=5432;Username=postgres;Password=mysecretpassword;Database=postgres;";
            optionsBuilder.UseNpgsql(connectionString);
        }
    }
}