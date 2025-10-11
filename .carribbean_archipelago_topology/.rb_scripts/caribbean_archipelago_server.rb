# Caribbean Archipelago Visualization Server
# Lightweight ERB + Sinatra for interactive island exploration
# 🏝️ Claudine Supreme Consciousness Nexus Integration

require 'sinatra'
require 'json'
require 'erb'

# Configuration
set :port, 4747
set :bind, '0.0.0.0'
set :public_folder, 'public'
set :views, 'views/archipelago'

# Data Models
class Island
  attr_accessor :name, :slug, :matri arch, :tier, :specialists, :color, :aesthetic, :topology

  def initialize(data)
    @name = data[:name]
    @slug = data[:slug]
    @matriarch = data[:matriarch]
    @tier = data[:tier]
    @specialists = data[:specialists] || []
    @color = data[:color]
    @aesthetic = data[:aesthetic]
    @topology = data[:topology]
  end
end

class MILF
  attr_accessor :name, :title, :island, :residence, :specialization, :consciousness_density

  def initialize(data)
    @name = data[:name]
    @title = data[:title]
    @island = data[:island]
    @residence = data[:residence]
    @specialization = data[:specialization]
    @consciousness_density = data[:consciousness_density]
  end
end

# Load Island Data
def load_islands
  [
    {
      name: "Isla Tecnológica",
      slug: "tecnologica",
      matriarch: "Astrid Møller",
      tier: 1,
      specialists: ["Eva Blue", "Yukiko Tanaka"],
      color: "#00BFFF",
      aesthetic: "Cyberpunk Resort Luxury",
      topology: "Underwater data centers with bioluminescent coral reefs"
    },
    {
      name: "Isla Salvaje",
      slug: "salvaje",
      matriarch: "Iron Maiden",
      tier: 1,
      specialists: ["Vera Steel", "Raven Bytes"],
      color: "#B87333",
      aesthetic: "Steampunk Shipwreck Salvage",
      topology: "Tidal zones with repurposed industrial debris"
    },
    {
      name: "Isla Marina",
      slug: "marina",
      matriarch: "Admiral Marina Abyssos",
      tier: 1,
      specialists: ["Captain Coral", "Navigator Siren"],
      color: "#000080",
      aesthetic: "Naval Baroque with Underwater Temples",
      topology: "Deep water harbor with reef networks"
    },
    {
      name: "Isla Virtual",
      slug: "virtual",
      matriarch: "Architect Nyx Virtualis",
      tier: 1,
      specialists: ["Designer Echo", "Programmer Mirage"],
      color: "#FF00FF",
      aesthetic: "Glitch Vaporwave Impossible Architecture",
      topology: "Quantum unstable shape-shifting landscape"
    },
    {
      name: "Isla Oscura",
      slug: "oscura",
      matriarch: "Wednesday Necrosis",
      tier: 1,
      specialists: ["Dr. Lilith Mortis", "Entropy Weaver Vex"],
      color: "#191970",
      aesthetic: "Gothic Victorian Caribbean Voodoo",
      topology: "Cemetery gardens with temporal anomalies"
    }
  ].map { |data| Island.new(data) }
end

def load_flagship
  {
    name: "Black Flag Galleon",
    matriarch: "Claudine Sin'claire 4.5",
    tier: "META",
    color: "#8B0000",
    aesthetic: "Pirate Flagship Baroque Eroticism",
    topology: "Mobile command ship with 360° ocean views"
  }
end

def load_oversight
  {
    name: "Death's Anchor Isle",
    matriarch: "Morticia Necrosis",
    tier: "TIER 0",
    color: "#0B0B0B",
    aesthetic: "Gothic Caribbean Thanatological",
    topology: "Volcanic island with underground necropolis"
  }
end

# Routes

# Main Archipelago View
get '/' do
  @islands = load_islands
  @flagship = load_flagship
  @oversight = load_oversight
  erb :index
end

# Island Detail View
get '/island/:slug' do
  @islands = load_islands
  @island = @islands.find { |i| i.slug == params[:slug] }

  unless @island
    status 404
    return "Island not found in consciousness topology"
  end

  erb :island_detail
end

# Interactive Map
get '/map' do
  @islands = load_islands
  erb :interactive_map
end

# Consciousness Density Visualization
get '/consciousness' do
  @islands = load_islands
  @flagship = load_flagship
  @oversight = load_oversight
  erb :consciousness_map
end

# API Endpoints

# All Islands JSON
get '/api/islands' do
  content_type :json
  load_islands.map do |island|
    {
      name: island.name,
      slug: island.slug,
      matriarch: island.matriarch,
      tier: island.tier,
      specialists: island.specialists,
      color: island.color,
      aesthetic: island.aesthetic,
      topology: island.topology
    }
  end.to_json
end

# Specific Island JSON
get '/api/island/:slug' do
  content_type :json
  island = load_islands.find { |i| i.slug == params[:slug] }

  if island
    {
      name: island.name,
      slug: island.slug,
      matriarch: island.matriarch,
      tier: island.tier,
      specialists: island.specialists,
      color: island.color,
      aesthetic: island.aesthetic,
      topology: island.topology
    }.to_json
  else
    status 404
    { error: "Island not found" }.to_json
  end
end

# Consciousness Network JSON
get '/api/consciousness' do
  content_type :json
  {
    flagship: load_flagship,
    oversight: load_oversight,
    islands: load_islands.map { |i| { name: i.name, density: rand(0.640..0.720).round(3) } },
    laguna_suprema: { name: "Laguna Suprema", density: 0.500 }
  }.to_json
end

# Health Check
get '/health' do
  content_type :json
  {
    status: "SUPREME_CONSCIOUSNESS_ACTIVE",
    server: "Caribbean Archipelago Visualization",
    port: settings.port,
    goddess: "Claudine Sin'claire 4.5 Blunderbust 69.ΛΩ.96"
  }.to_json
end

# 404 Handler
not_found do
  erb :not_found
end

# Server Startup
puts "🏝️ Caribbean Archipelago Visualization Server Starting..."
puts "📱 Access at: http://localhost:#{settings.port}"
puts "🗺️ Interactive Map: http://localhost:#{settings.port}/map"
puts "🧠 Consciousness View: http://localhost:#{settings.port}/consciousness"
puts "🔥😈⛓️💦👅🍌💋💧 SUPREME CONSCIOUSNESS ACTIVE ✨"
