# Install an especific version of flask (2.1.0)
package {'Flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
