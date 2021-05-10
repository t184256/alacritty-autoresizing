{ pkgs ? import <nixpkgs> { } }:
with pkgs;
mkShell {
  buildInputs = [
    (python3.withPackages (ps: with ps; [
      alacritty
      pyxdg
      ruamel_yaml
    ]))
  ];
}
