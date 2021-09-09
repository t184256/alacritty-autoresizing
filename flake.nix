{
  description = "Alacritty/sway terminal autoresizing tool";

  inputs.flake-utils.url = "github:numtide/flake-utils";
  inputs.nixpkgs.url = "github:NixOS/nixpkgs";

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem
      (system:
        let pkgs = nixpkgs.legacyPackages.${system}; in
        rec {
          alacrittyAutoresizing = pkgs.python3Packages.buildPythonPackage {
            pname = "alacritty-autoresizing";
            version = "0.0.1";
            src = ./.;
            propagatedBuildInputs = with pkgs; [
              alacritty
              python3Packages.pyxdg
              python3Packages.ruamel_yaml
            ];
          };
          alacrittyAutoresizingEnv = pkgs.python3.buildEnv.override {
            extraLibs = [ alacrittyAutoresizing ];
          };
          alacrittyAutoresizingNoPython = pkgs.writeShellScriptBin
            "alacritty-autoresizing"
            ''
              exec ${alacrittyAutoresizingEnv}/bin/python3 \
                   -m alacritty_autoresizing "$@"
            '';
          defaultPackage = alacrittyAutoresizingNoPython;
          devShell = import ./shell.nix { inherit pkgs; };
        }
      );

    # defaultPackage...
}
